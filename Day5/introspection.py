class Animal:
    """"
    This is an animal class and is being used as an example
    """

    def __init__(self, animal_type, sound):
        self.animal_type = animal_type
        self.sound = sound

    def print_animal_attributes(self):
        print("Animal attributes:", self.animal_type, self.sound)

    def __repr__(self):
        return "Animal attributes Repr:" + self.animal_type + self.sound


def main():
    animal1= Animal("Dog", "Bark")
    animal2 = Animal("Dog", "Bark")
    animal3 = animal2
    print(id(animal1))
    print(id(animal2))
    print(id(animal3))
    # print(dir(animal1))
    num = 5
    # print(dir(num))
    '''
    my_str = "superclass"
    print(len(dir(my_str)))
    print(my_str.__contains__("Mini"))
    print(my_str.__eq__("Max"))
    print(my_str.__len__())
    print(type(my_str))
    print(type(animal1))
    '''
    print(Animal.__doc__)
    print(Animal.__name__)
    print(hasattr(animal1, "print_animal_attributes"))
    print(getattr(animal1, "sound"))
    print(repr(animal1))
    animal1.print_animal_attributes()

if __name__ == "__main__":
    main()