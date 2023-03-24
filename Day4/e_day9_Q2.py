# Implement Hierarchical Inheritance with 3 classes and show how do protected and private
# variables and methods behave with an example.


class Vehicle:
    def __init__(self, num_of_wheels, engine_power, vehicle_type):
        self.__vehicle_type = vehicle_type
        self.num_of_wheels = num_of_wheels
        self.engine_power = engine_power
        self._vehicle_type = vehicle_type

    def __print_vehicle_attribute(self):
        print("vehicle attributes:", self.num_of_wheels, self.vehicle_type, self.engine_power)

    @property
    def vehicle_type(self):
        return self._vehicle_type


class Car(Vehicle):
    def __init__(self, num_of_wheels, engine_power, vehicle_type, color):
        super().__init__(num_of_wheels, engine_power, vehicle_type)
        self.color = color

    def print_car_attributes(self):
        print("car attributes:", self.num_of_wheels, self.engine_power, self.vehicle_type, self.color)

class Truck(Vehicle):
    def __init__(self, num_of_wheels, engine_power, vehicle_type, load_capacity):
        super.__init__(num_of_wheels, engine_power, vehicle_type)
        self._Truck__vehicle_type = None
        self.load_capacity = load_capacity

    def print_truck_attributes(self):
        print("truck attributes:", self.num_of_wheels,  self.vehicle_type, self.engine_power, self.load_capacity)


def main():
    vehicle = Vehicle(4, "car", 1200)
    car = Car(5, 1300, "truck", "white")
    # truck = Truck(10, 1500, "truck", 1500)
    print(vehicle.vehicle_type)



if __name__ =="__main__":
    main()