# Create a Calculator class that only has add and subtract functionality
# in which we can pass 2 numbers or 3 numbers as arguments to the addNumbers or subtractNumbers methods.
# Try using default values in the method or the dispatch keyword.
from multipledispatch import dispatch
class Calculator:
    # def __init__(self, num1, num2):
    #     self.num1 = num1
    #     self.num2 = num2

    @dispatch(int, int)
    def sub(self, a, b=1):
        return a - b

    @dispatch(int, float, int)
    def add(self, a, b, c=1):
        return a + b + c


    @dispatch(int, int)
    def  add(self, a, b=1):
        return a + b

    @dispatch(int, float, int)
    def sub(self, a, b, c=1):
        return a - b - c

def main():
    calculator = Calculator()
    print(calculator.sub(2, 3))
    print(calculator.add(1, 2.2, 3))
    print(calculator.sub(7, 2.2 ,1 ))
    print(calculator.add(5, 3))

if __name__ =="__main__":
    main()