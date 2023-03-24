class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.__marks = marks

def main():
    student1 = Student("Ram", 17, 100)
    print(student1.age)
    # print(student1.__marks)
# private variables that access by using this above condition
    print(student1._Student__marks)
    # for accessing private variable values

#
# for accessing the private variables
#     print(object_name._classname__private variablename)







if __name__ =="__main__":
    main()

