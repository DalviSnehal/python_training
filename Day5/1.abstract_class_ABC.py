from abc import ABC, abstractmethod

#Abstraction is used to hide the internal functionality of the function from the users

class Shape(ABC):
    @abstractmethod
    def has_shape(self):
        pass


    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def has_shape(self):
        print("This shape is circle")

    def calculate_area(self):
        print("The area of circle is:", 3.14*self.radius*self.radius)

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def has_shape(self):
        print("This shape is Rectangle.")

    def calculate_area(self):
        print("The area of rectangle is:", self.length * self.breadth)

def main():
    circle = Circle(3)
    circle.has_shape()
    circle.calculate_area()
    rect = Rectangle(3, 4)
    rect.has_shape()
    rect.calculate_area()

if __name__ ==  "__main__":
    main()