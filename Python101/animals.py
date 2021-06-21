from animal import Animal
from fight import Fight
from random import randrange
from random import shuffle

class Animals:
    listOfAnimalNames = [
        "Hest",
        "Ku",
        "Flodhest",
        "Esel",
        "Hund",
        "Katt",
        "Skilpadde",
        "Elg",
        "Hybelkanin",
        "Martin"
    ]


    animals = []

    def __init__(self, numberOfAnimals):
        self.numberOfAnimals = numberOfAnimals
        self.createAnimals()

    def createAnimals(self):
        for i in range(0, self.numberOfAnimals):
            name = self.listOfAnimalNames[randrange(len(self.listOfAnimalNames))]
            hp = randrange(70, 130)
            ap = randrange(10, 40)
            self.animals.append(Animal(name, hp, ap))

    def printAnimals(self):
        print(f"{'Species':15} | {'AP':2} | {'HP':2}")
        print("-----------------------------")
        for animal in self.animals:
            print(f"{animal.name:15} | {str(animal.getAp()):2} | {str(animal.getHp()):2}")
        print("-----------------------------")

    def fight(self):
        while len(self.animals) > 1:
            shuffle(self.animals)
            self.printAnimals()
            pairs = []
            for i in range(1, len(self.animals), 2):
                pair = []
                pair.append(self.animals[i - 1])
                pair.append(self.animals[i])
                pairs.append(pair)

            if len(self.animals) % 2 == 0:
                self.animals.clear()
            else:
                for i in range(len(self.animals) - 2, 0, -1):
                    self.animals.pop(i)

            for pair in pairs:
                while True:
                    print("\n\n")
                    print(f"Fight between {pair[0].getName()} and {pair[1].getName()}")
                    input("Any input ")
                    Fight(pair[0], pair[1])
                    print(f"{'Species':15} | {'AP':2} | {'HP':2}")
                    print(f"{pair[0].getName():15} | {str(pair[0].getAp()):2} | {str(pair[0].getHp()):2}")
                    print(f"{pair[1].getName():15} | {str(pair[1].getAp()):2} | {str(pair[1].getHp()):2}")
                    if pair[0].getHp() < 0 and pair[1].getHp() < 0:
                        del pair[1]
                        del pair[0]
                        break
                    elif pair[0].getHp() <= 0:
                        print(f"\n{pair[0].getName()} died!")
                        del(pair[0])
                        self.animals.append(pair[0])
                        break
                    elif pair[1].getHp() <= 0:
                        print(f"\n{pair[1].getName()} died!")
                        del(pair[1])
                        self.animals.append(pair[0])
                        break
