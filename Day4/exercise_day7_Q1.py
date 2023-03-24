# Write any class of your choice and create a child class of it using single inheritance


class Animal:
    def __init__(self,age, name):
        self.age= age
        self.name = name
    def print_age(self):
        print(self.age)
    def print_name(self):
        print(self.name)

class Dog(Animal):
    def __init__(self, age, name, sound):
        super().__init__(age, name)
        self.sound = sound

    def print_sound(self):
        print(self.sound)

def main():
    dog = Dog(5, "rocky", "high")
    dog.print_sound()
    dog.print_age()
    dog.print_name()

if __name__ == "__main__":
    main()
