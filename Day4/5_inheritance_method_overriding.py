class Shape:
    def __init__(self, sides):
        self.sides = sides


    def print_shape(self):
        print("this shape is not defined")

    def print_sides(self):
        print(self.sides)

class Square(Shape):
    def __init__(self, sides):
        super().__init__(sides)

    def print_shape(self):
        print("this shape is square")


class Circle(Square):
    def __init__(self, sides):
        self.sides = sides

    def print_Shape(self):
        print("this shape is circle")



class Triangle(Circle):
    def __init__(self):
        pass

def main():
    circle = Circle(3)
    square = Square(4)
    square.print_shape()
    square.print_sides()
    circle.print_sides()
    triangle = Triangle()
    triangle.print_shape()

if __name__ =="__main__":
    main()