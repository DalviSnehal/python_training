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
        print("car attributes:", self.num_of_wheels, self.engine_power, self.vehicle_type, self.color)

class Truck(Vehicle):
    def __init__(self, num_of_wheels, engine_power, vehicle_type, load_capacity):
        super.__init__(num_of_wheels, engine_power, vehicle_type)
        self.load_capacity = load_capacity

    def print_truck_attributes(self):
        print("truck attributes:", self.num_of_wheels,  self.vehicle_type, self.engine_power, self.load_capacity)

def main():
    car = Car(4, 1200, "car", "red")
    car.print_car_attributes()
    car.print_vehicle_attribute()
    truck = Truck(4, 1300, "eicher", "2500_tone")
    truck.print_truck_attributes()
    truck.print_vehicle_attribute()

if __name__ =="__main__":
    main()