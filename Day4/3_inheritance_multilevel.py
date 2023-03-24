class Vehicle:
    def __init__(self, num_of_wheels, engine_power, vehicle_type):
        self.num_of_wheels = num_of_wheels
        self.engine_power = engine_power
        self.vehicle_type = vehicle_type

    def print_vehicle_attribute(self):
        print("vehicle attributes:", self.num_of_wheels, self.vehicle_type, self.engine_power)

class Car(Vehicle):
    def __init__(self, num_of_wheels, engine_power, vehicle_type, color):
        super().__init__(num_of_wheels, engine_power, vehicle_type)
        self.color = color

    def print_car_attributes(self):
        print("car attributes:",self.num_of_wheels, self.engine_power, self.vehicle_type, self.color)

class SportsCar(Car):
    def __init__(self, num_of_wheels, engine_power, vehicle_type, color, turbo_acc):
        super().__init__(num_of_wheels, engine_power, vehicle_type, color)
        self.turbo_acc = turbo_acc

    def print_sportscar_attributes(self):
        print("sportscar attributes:", self.num_of_wheels, self.engine_power, self.vehicle_type, self.color, self.turbo_acc)


def main():
    car = Car(4, 1200, "car" ,"red")
    car.print_car_attributes()
    sportscar = SportsCar(4, 1300, "i10", "Blue", 2333)
    sportscar.print_vehicle_attribute()
    sportscar.print_sportscar_attributes()
    sportscar.print_car_attributes()




if __name__ =="__main__":
    main()