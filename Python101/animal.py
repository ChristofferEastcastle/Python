from random import randrange

class Animal:
    def __init__(self, name, hp, ap):
        self.name = name
        self.hp = hp
        self.ap = ap

    def takeDamage(self, damage):
        self.hp -= damage

    def heal(self, health):
        self.hp += health

    def attack(self):
        random = randrange(0, 8)
        if random == 0:
            return self.ap * 0
        elif random < 8:
            return self.ap * 1
        else:
            return self.ap * 2


    def getName(self):
        return self.name

    def getHp(self):
        return self.hp

    def getAp(self):
        return self.ap