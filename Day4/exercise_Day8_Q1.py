# Write a parent and child class Shape and Rectangle. Create 3 instance attributes in
# the constructor for Shape (height, width, shape_name). Create methods in Shape for display_attributes
# and number_of_sides override it in Rectangle

class Shape:
    def __init__(self, height, width, shape_name, sides):
        self.height = height
        self.width = width
        self.shape_name = shape_name
        self.sides = sides

    def display_attribute(self):
        print("attributes of shapes are:", self.height, self.width, self.shape_name)

    def number_of_sides(self):
        print("no of sides are:", self.sides)



class Rectangle(Shape):
    def __init__(self, height, width, shape_name, sides):
        super().__init__(height, width, shape_name, sides)


    def display_attribute(self):
        print("attributes of rectangle are:", self.height, self.width, self.shape_name)

    def number_of_sides(self):
        print("no of sides of rectangle are:", self.sides)

def main():
    shape = Shape(4, 5, "square", 5)
    rectangle = Rectangle(4, 4, "rectangle", 4)
    shape.display_attribute()
    rectangle.display_attribute()
    rectangle.number_of_sides()


if __name__ == "__main__":
    main()