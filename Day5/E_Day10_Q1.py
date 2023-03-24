#
# Implement Hybrid Inheritance using any class of your choice (examples: Shape, Animal etc)
class Shape:
    def print_method(self):
        print("This is shape:")

class Square(Shape):
    def print_method(self):
        print("This is square:")

class Rectangle(Shape):
    def print_method(self):
        print("This is Rectangle:")

class Rhombus(Square, Rectangle):
    def print_method(self):
        print("This is Rhombus:")

def main():
  rhombus = Rhombus()
  rhombus.print_method()

if __name__ =="__main__":
    main()