class Student:
    school_name = "DEF school"

    def __init__(self, name):
        self.name = name

def another_change_school_name(cls, school_name):
    cls.school_name = school_name

def main():
    student = Student("Ram")
    Student.another_change_school_name = classmethod(another_change_school_name)
    Student.another_change_school_name("Abc school")
    print(Student.school_name)





if __name__ =="__main__":
    main()