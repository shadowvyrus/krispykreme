from Person import *
from login import *
import random
import smtplib, ssl
import csv

"""
TODO
- complete email functionality
"""

THRESHOLD = 1.5 # range of this value is (1, len(self.people) // 2]

class KrisKringle:
    def __init__(self):
        self.people = []

    def get_people(self):
        return self.people

    def add_person(self, name, email):
        # replace to remove BOM in csv file if present
        new_person = Person(name.replace(u'\ufeff', ''), email)
        self.people.append(new_person)

    # csv format: name, email
    # no header required
    def import_csv(self, filename):
        with open(filename) as f:
            for line in f:
                name, email = line.strip().replace('"', '').split(',')
                self.add_person(name, email)

    # each person sends a gift to the next person in the list
    # last person is gifter for first person in list
    def shuffle_people(self):
        shuffled = False

        # temp assignment using original list
        for i in range(len(self.people)):
            try:
                self.people[i].set_assigned(self.people[i+1].get_name())
            except IndexError:
                self.people[i].set_assigned(self.people[0].get_name())
        
        while not shuffled:
            temp = random.sample(self.people, k = len(self.people))
            
            score = self.calc_dissimilarity_score(temp)

            if score > THRESHOLD:
                shuffled = True
                self.people = temp

    # saving order of participants for subsequent years   
    def save_config(self, filename):
        with open(filename, 'w') as f:
            csv_output = csv.writer(f)
            for person in self.people:
                csv_output.writerow([person.get_name(), person.get_email()])

    def print_people(self):
        for person in self.people:
            print(person.get_name())

    def send_email(person,person2):
        receiver_email = "spencer_xu@y7mail.com"  # Enter receiver address, change to person1.email or something
        message = """\
        Subject: Hi there

        This message is sent from Python."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
            server.login(SENDER_EMAIL, PASSWORD)
            server.sendmail(SENDER_EMAIL, receiver_email, message)

    def send_all_emails(self):
        for i in self.people:
            try:
                self.send_email(self.people[i],self.people[i+1])
            except IndexError:
                self.send_email(self.people[i],self.people[0])
    
    # calculate by how much a new order differs from the previous order
    def calc_dissimilarity_score(self, new_list):
        score = 0
        new_list_length = len(new_list)

        # loop through each person in the new list
        for i in range(new_list_length):
            assigned = new_list[i].get_assigned()
            assigned_idx = self.find_person(assigned, new_list)

            # score is distance between a person and assigned in a directed graph
            temp_score = assigned_idx - i
            score += temp_score if assigned_idx > i else new_list_length - temp_score

        return score
    
    # helper function for finding location of person in a given list
    def find_person(self, name, search_list):
        for i in range(len(search_list)):
            if search_list[i].get_name() == name:
                return i

# debug
if __name__ == "__main__":
    kk = KrisKringle()

    kk.import_csv('krispykremeTest.csv')
    kk.print_people()
    kk.shuffle_people()