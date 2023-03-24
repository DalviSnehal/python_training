# Add a private attribute to the Animal class defined above named can_swim(boolean) and define a getter and setter method for the same.


class Animal:
    def __init__(self, sound, number_of_legs, is_omnivore, can_swim):
        self.sound = sound
        self.__number_of_legs = number_of_legs
        self.is_omnivore = is_omnivore
        self.__can_swim = can_swim

    def get_value_can_swim(self):
        return self.__can_swim


    def set_value_can_swim(self, can_swim):
        # if self.__number_of_legs < 4:
        #     return "Animal can not swim"
        # else:
        #     self.__can_swim = can_swim
        #     return "set succcessfully"
        print(self.__can_swim)


def main():
    animal1=Animal("high", 4, True, "no")
    print(animal1.get_value_can_swim())
    animal1.set_value_can_swim("yes")
    print(animal1.get_value_can_swim())




if __name__ =="__main__":
    main()