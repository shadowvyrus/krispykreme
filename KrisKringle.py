from Person import *
import random

"""
TODO
- email participants
"""

class KrisKringle:
    def __init__(self):
        self.people = []

    def get_people(self):
        return self.people

    def add_person(self, name, email):
        new_person = Person(name, email)
        self.people.append(new_person)

    # csv format: name, email
    # no header required
    def import_from_csv(self, filename):
        with open(filename) as f:
            for line in f:
                name, email = line.split(',')
                self.add_person(name, email)

    # each person sends a gift to the next person in the list
    # last person is gifter for first person in list
    def shuffle_people(self):
        shuffled = False
        while not shuffled:
            temp = self.people[:]
            random.shuffle(self.people)

            if temp != self.people:
                shuffled = True
        
    def print_people(self):
        for person in self.people:
            print(person.get_name())

    def print_assigned(self):
        raise NotImplementedError()

# debug
if __name__ == "__main__":
    kk = KrisKringle()

    kk.import_from_csv('krispykremeTest.csv')
    kk.shuffle_people()
    kk.print_people()