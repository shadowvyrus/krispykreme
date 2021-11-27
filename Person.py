class Person:
    def __init__(self, name, email):
        self._name = name
        self._email = email
        self._assigned = None
        
    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_assigned(self):
        return self._assigned

    def set_assigned(self, assigned):
        self._assigned = assigned