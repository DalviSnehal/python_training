# liskov substitution principle
class Shape:
    def __init__(self, sides):
        self.sides = sides

    def print_shape(self):
        print("this shape is not defined")

class Square(Shape):
    def __init__(self, sides):
        super().__init__(sides)

    def print_shape(self, arg="default_arg"):
        print("this shape is a square:", arg)

class Triangle(Shape):
    def __init__(self, sides):
        super().__init__(sides)

    def print_shape(self, arg="default_arg_triangle"):
        print("this shape is triangle", arg)

def main():
    square = Square(4)
    shape = Shape(5)
    triangle = Triangle(3)
    shape_list = [square, shape, triangle]
    for shape_obj in shape_list:
        print_shape_wrapper(shape_obj)


def print_shape_wrapper(obj):
    obj.print_shape()


if __name__ =="__main__":
    main()


