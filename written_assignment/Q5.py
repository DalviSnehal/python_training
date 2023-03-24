# 5. What is polymorphism? Create 2 classes Shape and Circle with the same instance variables and
# methods and show how does Python use polymorphism by utilising objects of those classes.

class Shape:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)

    def make_shape(self):
        print("rectangle")


class Circle:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)

    def make_shape(self):
        print("circle")

def main():
    shape1 = Shape("rectangle", 2.5)
    circle1 = Circle("circle", 4)
    print(shape1.make_shape())
    print(shape1.info())
    print(circle1.info())
    print(circle1.make_shape())

if __name__ == "__main__":
        main()