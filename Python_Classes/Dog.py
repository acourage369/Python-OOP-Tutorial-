from Animal import Animal


class Dog(Animal):
    def __init__(self, height, breed, cry):
        super().__init__(height, breed, cry)

    def get_animal_cry(self):
        return self.cry

    def set_animal_cry(self, cry):
        self.cry = cry
