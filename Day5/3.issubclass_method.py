class Animal:
    def __init__(self, animal_type, sound):
        self.animal_type = animal_type
        self.sound = sound

class Dog(Animal):
    def __init__(self, animal_type, sound, breed):
        super().__init__(animal_type, sound)
        self.breed = breed

class StreetDog(Dog):
    def __init__(self, animal_type, sound, breed):
        super().__init__(animal_type, sound, breed)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def main():
    animal = Animal("Cat", "Meow")
    dog = Dog("Dog", "Bark", "Husky")
    person = Person("Ram", 18)
    print(issubclass(Dog, Animal))
    print(issubclass(StreetDog, Animal))
    print(issubclass(Animal, Dog))
    print(issubclass(Dog, Person))
    print(issubclass(Animal, Person))
    # print(issubclass(dog, animal))




if __name__ == "__main__":
    main()