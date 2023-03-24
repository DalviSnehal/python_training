# In the above Number class override the in-built method for __add__ so that when we add two numbers they should return the sum of their values, override the below methods as well:
# Addition
# +
# __add__(self, other)
# Subtraction
# -
# __sub__(self, other)
# Multiplication
# *
# __mul__(self, other)
# Division
# /
# __div__(self, other)
# Floor Division
# //
# __floordiv__(self,other)
# Modulus
# %
# __mod__(self, other)
# Power
# **
# __pow__(self, other)
#
#

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __mul__(self, other):
        return self.value * (other.value)

    def __truediv__(self, other):
        return self.value / (other.value)

    def __mod__(self, other):
        return self.value % (other.value)

    def __floordiv__(self, other):
        return self.value // (other.value)

def main():
    number1 = Number(2)
    number2 = Number(5)
    print(number1 + number2)
    print(number1 * number2)
    print(number1 // (number2))
    print(number1 / number2)
    print(number1 % number2)

if __name__ == "__main__":
    main()