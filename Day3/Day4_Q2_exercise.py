# Create a class named Number which has object attributes called datatype(string) and value(can be int/float),
# create getter and setter methods for datatype and value. Add the constraint that if the datatype is changed from
# int to float then the value should also be typecast to float, and if the value is changed then the datatype is also
# changed (Example: if datatype = int and value = 2, and using the setter method we change datatype to float then
# value should become 2.0, and if value is changed from 2.0(float) to 3(int) change datatype from float to int)


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


def main():
    number = Number("int", 2)
    print(number.get_value())
    print(number.get_datatype())
    print(number.set_datatype("float"))
    print(number.get_datatype())
    print(number.set_value(2.2))
    print(number.get_value())


if __name__ == "__main__":
    main()
