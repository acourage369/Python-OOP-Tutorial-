from shape import Shape


class Rectangle(Shape):

    def __init__(self, width, height, name):
        super().__init__(name)
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def calculate_perimeter(self):
        return round(2 * (self.width + self.height))

    def calculate_area(self):
        return round(self.width * self.height)

