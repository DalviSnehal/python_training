# Polymorphism is a programming term that refers to the use of the
# same function name, but with different signatures,
# The best example of polymorphism is human behavior. One person can have different behavior.
# For example, a person acts as an employee in the office,
# a customer in the shopping mall, a passenger in bus/train, a student in school, and a son at home
class Vehicle:
    def __init__(self, color, make):
        self.color = color
        self.make = make

    def get_color(self):
        return self.color

    def get_make(self):
        return self.make



class Car:
    def __init__(self, color, make):
        self.color = color
        self.make = make

    def get_color(self):
        return self.color

    def get_make(self):
        return self.make


def main():
    vehicle1 = Vehicle("red", "bmw")
    car1 = Car("blue", "altroz")
    for obj in (vehicle1, car1):
        print(obj.get_make(), obj.get_color())


if __name__ == "__main__":
    main()
