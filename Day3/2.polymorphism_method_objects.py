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

def print_values(obj):
    print(obj.get_make(), obj.get_color())

def main():
    vehicle = Vehicle("red", "bmw")
    car = Car("pink", "scorpio")
    print_values(vehicle)
    print_values(car)



if __name__ =="__main__":
    main()