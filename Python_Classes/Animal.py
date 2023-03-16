from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, height, breed, cry):
        self.height = height
        self.breed = breed
        self.cry = cry

    def set_height(self, height):
        self.height = height

    def set_breed(self, breed):
        self.breed = breed

    def get_height(self):
        return self.height

    def get_breed(self):
        return self.breed

    @abstractmethod
    def set_animal_cry(self, cry):
        pass

    @abstractmethod
    def get_animal_cry(self):
        pass
