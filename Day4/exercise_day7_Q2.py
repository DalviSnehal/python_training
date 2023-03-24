# # Write any 3 classes of your choice to showcase multilevel inheritance.
class Animal:
    def __init__(self, age):
        self.age = age
    def print_age(self):
        print(self.age)

class Dog(Animal):
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name

    def print_name(self):
        print(self.name)

class Cat(Dog):
    def __init__(self, age, name, sound):
        super().__init__(age, name)
        self.sound = sound

    def print_sound(self):
        print(self.sound)

def main():
    dog= Dog(5, "rocky")
    dog.print_name()
    dog.print_age()
    cat = Cat(5, "cutie", "low")
    cat.print_sound()
    cat.print_name()
    cat.print_age()




if __name__ == "__main__":
    main()

