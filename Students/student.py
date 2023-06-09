class Student:

    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grades(self):
        return self.grades

    def average(self):
        return sum(self.grades) / len(self.grades)
