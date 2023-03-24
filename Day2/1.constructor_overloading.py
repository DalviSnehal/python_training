
# python doesnt support constructor overloadding
# overloading when we use the same function name but the different arguments?

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __int__(self):
        self.name = "random name"




def main():
    student = Student()
    print("object is created")



if __name__ =="__main__":
    main()