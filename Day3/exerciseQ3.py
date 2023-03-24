# In the above Number class override the in-built method for __add__ so that when we add two
# numbers they should return the sum of their values, override the below methods as well:
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

class Number:
    def __init__(self, datatype, value):
        self.datatype = datatype
        self.value = value


    def get_value(self):
        return self.value

    def get_datatype(self):
        return self.datatype

    def set_datatype(self, datatype):
        if datatype == self.datatype:
            pass
        else:
            if datatype == "float":
                self.value = float(self.value)
            else:
                self.value = int(self.value)

    def set_value(self, value):
        if self.datatype == type(value):
            self.value = value
        else:
            self.datatype = str(type(value))
            self.value = value

class Operation:
    def __init__(self, value1):
        self. value1 = value1

    def get_value1(self):
        return self.value1

    def __add__(self, other):
        return self.get_value1() + other.get_value()


    def __mul__(self, other):
        return self.get_value1() * (other.get_value())


    def __mod__(self, other):
        return self.get_value1() % (other.get_value())

    def __floordiv__(self, other):
        return self.get_value1() // (other.get_value())

    def __pow__(self, other):
        return self.get_value1()  (other.get_value())



def main():
    number = Number("int", 27)
    # print(number.get_value())
    # print(number.get_datatype())
    # print(number.set_datatype("float"))
    # print(number.get_datatype())
    # print(number.set_value(2.2))
    # print(number.get_value())
    operation = Operation(3)
    print(operation + number)
    print(operation * number)
    print(operation % number)
    print(operation // number)

if __name__ =="__main__":
    main()

