class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.send = None
        self.receive = None

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_send(self):
        return self.send

    def get_receive(self):
        return self.receive

    def set_send(self, name):
        self.send = name

    def set_receive(self, name):
        self.receive = name