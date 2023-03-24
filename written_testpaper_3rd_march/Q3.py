# 3. What is the super keyword and where is it used? Write code examples showing its use cases
class Animal:
    def __init__(self, num_of_legs, sound):
        self.num_of_legs = num_of_legs
        self.sound = sound

    def print_sound(self):
        print("Animal:", self.sound)

    def print_num_of_legs(self):
        print("Animal", self.num_of_legs)

class Dog(Animal):
    def __init__(self, num_of_legs, sound, has_collar):
        super().__init__(num_of_legs, sound)
        self.has_collar = has_collar

    def print_sound(self):
        super().print_sound()
        print("Hello world")
        super().print_num_of_legs()

def main():
    dog = Dog(4, "woof", True)
    dog.print_sound()




if __name__ == "__main__":
    main()
