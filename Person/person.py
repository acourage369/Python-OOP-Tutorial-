class Person:

    def __init__(self, first_name, last_name, age, gender, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.phone = phone

    def get_name(self):
        return self.first_name+' '+self.last_name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_phone(self):
        return self.phone
