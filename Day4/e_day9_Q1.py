#
# Implement Multilevel Inheritance with any classes of your choice and show
# how does inheritance in classmethods work with an example

class Vehicle:
    no_of_wheels = 4
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    @classmethod
    def change_no_of_wheels(cls, no_of_wheels):
        cls.no_of_wheels = no_of_wheels

class Car(Vehicle):
    def __init__(self, vehicle_type, color):
        super().__init__(vehicle_type)
        self.color = color


class SportsCar(Car):
    def __init__(self, vehicle_type, color, turbo_acc):
        super().__init__(vehicle_type, color)
        self.turbo_acc = turbo_acc



def main():
    vehicle = Vehicle("car")
    print(Vehicle.no_of_wheels)
    car = Car("scorpio", "red")
    Car.change_no_of_wheels(6)
    print(car.no_of_wheels)
    print(Car.no_of_wheels)
    sportscar = SportsCar("truck", "white", 1200)
    SportsCar.change_no_of_wheels(10)
    print(SportsCar.no_of_wheels)



if __name__ =="__main__":
    main()
