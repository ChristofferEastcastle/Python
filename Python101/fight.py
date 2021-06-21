from animal import Animal
from random import randrange
class Fight:
    def __init__(self, animal1: Animal, animal2: Animal):
        self.animal1 = animal1
        self.animal2 = animal2
        self.fighting()

    def fighting(self):
        self.animal1.takeDamage(self.animal1.attack())
        self.animal2.takeDamage(self.animal2.attack())