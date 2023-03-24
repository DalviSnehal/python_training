class Animal:
    def __init__(self, animal_type, sound):
        self.animal_type = animal_type
        self.sound = sound

class Dog(Animal):
    def __init__(self, animal_type, sound, breed):
        super().__init__(animal_type, sound)
        self.breed = breed

def main():
    # dog = Dog("Dog", "Bark", "Husky")
    # animal = Animal("Cat", "Meow")
    # print(isinstance(animal, Dog))
    # print(isinstance(animal, Animal))
    # print(isinstance(dog, Dog))
    # print(isinstance(dog, Animal))
    # print(isinstance(animal, list))

    num = 10
    float_num = 2.3
    my_list = ['a', 'b', 'c', 'd', 1, 1.5]
    my_string = "Random String"
    complex_num = complex(3, 4)
    print(isinstance(num, int))
    print(isinstance(num, float))
    print(isinstance(float_num, float))
    print(isinstance(float_num, list))
    print(isinstance(my_list, list))
    print(isinstance(my_string, str))
    print(isinstance(complex_num, complex))
    print(isinstance(complex_num, int))
    print(type(num))




if __name__ == "__main__":
    main()