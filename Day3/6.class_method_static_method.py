
class Student:
    school_name = "saraswati vidya mandir"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school_name(cls, school_name):
        cls.school_name = school_name

    @staticmethod
    def addition(a, b):
        return a + b

#    instance method
    def get_name(self):
        return self.name


def main():
    student1 = Student("Ram", 17)
    student2 = Student("shyam", 18)
    Student.change_school_name("abc")
    print(Student.school_name)


if __name__ =="__main__":
    main()