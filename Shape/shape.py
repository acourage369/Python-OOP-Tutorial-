from abc import ABC


class Shape(ABC):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass