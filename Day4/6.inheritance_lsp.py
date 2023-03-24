class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def set_length(self, length, breadth):
        self.length = length

    def set_breadth(self, breadth):
        self.breadth = breadth


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def set_length(self, length, breadth):
        self.length = self.breadth = length

    def set_breadth(self, breadth):
        self.length = self.breadth = breadth


def calculate_area(obj):
    obj.set_length(10, 20)
    return "area is" + str(10 * obj.breadth)


def main():
    rect = Rectangle(4,5)
    square = Square(4)
    print(calculate_area(rect))
    print(calculate_area(square))


if __name__ == "__main__":
    main()
# if we add third value in that method then we have to given the default argument