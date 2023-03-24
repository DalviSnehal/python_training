class Shape:
    def __init__(self, sides):
        self.sides = sides

    def print_sides(self):
        print(self.sides)

class Rectangle(Shape):
    def __init__(self, sides, length, breadth):
        super().__init__(sides)
        self.length = length
        self.breadth = breadth

    def print_length(self):
        print(self.length)

    def print_breadth(self):
        print(self.breadth)

def main():
    rect = Rectangle(4, 2, 2)
    # print(rect.sides)
    rect.print_sides()

    rect.print_breadth()
    rect.print_length()




if __name__ =="__main__":
    main()