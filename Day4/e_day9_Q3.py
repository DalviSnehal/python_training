# Create classes Animal and Dog with the following methods print_attributes,
# make_sound, display_colour, display_animal_type and write a method which takes in any
# object(Animal or Dog) and call all of the above methods
class Animal:
    def __init__(self, sound, color, type):
        self.sound = sound
        self.color = color
        self.type = type

    def print_attributes(self):
        print("animal attributes are:", self.sound, self.color, self.type)

    def make_sound(self):
        return True

    def display_color(self):
        print(self.color)

    def display_animal_type(self):
        print("animal type is", self.type)

class Dog(Animal):
    def __init__(self, sound, color, type):
        super().__init__(sound, color, type)

    def print_attributes(self):
        print("dog attributes are:", self.sound, self.color, self.type)

    def make_sound(self):
        return True

    def display_color(self):
        print(self.color)

    def display_animal_type(self):
        print("animal type is", self.type)

def show(obj):
    obj.print_attributes()
    obj.display_color()
    obj.display_animal_type()
    obj.make_sound()
def main():
    dog = Dog("high", "white", "dog")
    animal = Animal("low", "red", "animal")
    # dog.print_attributes()
    # dog.display_animal_type()
    # dog.display_color()
    # print(dog.make_sound())
    # animal.print_attributes()
    # animal.display_animal_type()
    print(show(dog))
    print(show(animal))
if __name__ =="__main__":
    main()