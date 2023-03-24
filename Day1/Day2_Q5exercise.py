# Modify the Animal class to count number of instances of the Animal class
class Animal:
    count=0
    def __init__(self, sound):
        self.sound = sound
        Animal.count=Animal.count+1


animal1 = Animal("Bark")
animal2 = Animal("moo")
animal3 = Animal("shouting")
animal4 = Animal("screeming")
print(animal1.count)


