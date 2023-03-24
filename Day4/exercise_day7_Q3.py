# Create any class of your choice and then create 3 child classes of it to exhibit hierarchical inheritance


class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name =name

    def print_animal_details(self):
        print("animal details are:" , self.age, self.name)

class Dog(Animal):
    def __init__(self, age, name, sound):
        super().__init__(age, name)
        self.sound = sound

    def print_dog_details(self):
        print("dog details are:", self.age, self.name, self.sound)

class Cat(Animal):
    def __init__(self, age, name, num_of_legs):
        super().__init__(age, name)
        self.num_of_legs = num_of_legs

    def print_cat_details(self):
        print("cat details are:", self.age, self.name, self.num_of_legs)

def main():
    animal = Animal(12, "dog")
    animal.print_animal_details()

    cat = Cat(13, "cat", 4)
    cat.print_cat_details()
    print("number of legs of cat", cat.num_of_legs)
    dog = Dog(12,"rocky", "high")
    dog.print_animal_details()


if __name__ == "__main__":
    main()