from shape import Shape
import math


class Circle(Shape):

    def __init__(self, radius, name):
        super().__init__(name)
        self.radius = radius

    def get_radius(self):
        return self.radius

    def calculate_area(self):
        return round(math.pi * pow(self.radius, 2))

    def calculate_perimeter(self):
        return round(2 * math.pi * self.radius)
