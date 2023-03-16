from animal import Animal


class Tiger(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        return "Growl"
