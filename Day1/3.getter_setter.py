class Student:
    def __init__(self, name, age, marks):
        self.__name=name
        self.__age=age
        self.__marks=marks
# __means private variable and this can access by using an creating get methods
    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if self.__age < 17:
            return "not allowed"
        else:
            self.__marks = marks
            return "set successfully"

def main():
    student1=Student("Ram", 17, 100)
    print(student1.get_marks())
    print(student1.set_marks(110))
    print(student1.get_marks())





if __name__ =="__main__":
    main()




