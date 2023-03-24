
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

def main():
    student1 = Student("Ram", 17)
    student2 = Student("Ram", 25)
    print(student1.age)
    del student1.age
    print(student1.name)
    del student1
    print(student1.age)



if __name__ =="__main__":
    main()

# del keyword is used to delete the object and variable
