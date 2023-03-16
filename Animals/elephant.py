from animal import Animal


class Elephant(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        return "Trumpet"

