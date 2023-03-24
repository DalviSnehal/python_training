# Create a method calculate_area in Shape class and override
# it in Rectangle and use the super keyword to help calculate the area


# Create a method calculatePerimeter and override it in Rectangle


class Shape:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return "area is", 2 * self.height * self.width

    def calculate_perimeter(self):
        return "perimeter is", self.height + self.width



class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__(height, width)

    def calculate_area(self):
        return super().calculate_area()

    def calculate_perimeter(self):
        return super().calculate_perimeter()




def main():
    shape = Shape(5, 6)
    rect = Rectangle(4, 5)
    print(rect.calculate_perimeter())
    print(rect.calculate_area())


if __name__ == "__main__":
    main()
