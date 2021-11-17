from Person import *
import random

"""
TODO
- allocation algorithm (sunny)
- email participants

"""

class KrisKringle:
    def __init__(self):
        self.people = []
        self.assigned = []

    def add_person(self, name, email):
        person = Person(name, email)
        self.people.append(person)

    def import_from_csv(self, filename):
        with open(filename) as f:
            for line in f:
                name, email = line.split(',')
                self.add_person(name, email)
    
    def print_people(self):
        for person in self.people:
            print(person.get_name())

    def pair_people(self):
        raise NotImplementedError

# debug
if __name__ == "__main__":
    kk = KrisKringle()

    kk.import_from_csv('krispykremeTest.csv')
    kk.print_people()