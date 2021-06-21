from animals import Animals

numberOfAnimals = input("How many animals? ")
animals: Animals = Animals(int(numberOfAnimals))

animals.fight()