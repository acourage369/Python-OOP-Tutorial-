from animal import Animal


class Lion(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        return "Roar"
