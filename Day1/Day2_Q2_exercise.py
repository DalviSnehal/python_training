
# Create a Animal class with attributes sound(string), number_of_legs(integer) and is_omnivore(boolean)
class Animal:
    def __init__(self, sound, number_of_legs, is_omnivore):
        self.sound = sound
        self.number_of_legs = number_of_legs
        self.is_omnivore = is_omnivore

def main():
    animal1 = Animal("high", 4, True)
    print(animal1.sound, animal1.number_of_legs, animal1.is_omnivore)





if __name__ =="__main__":
    main()