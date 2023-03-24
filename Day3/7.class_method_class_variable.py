class Student:
    school_name = "DEF school"#class variable

    def __init__(self, name):
        self.name = name


    @classmethod
    def change_school_name(cls, school_name):
        cls.school_name = school_name

    @classmethod
    def fetch_school_name(cls):
        return cls.school_name

    def get_name(self):
        return self.name

def main():
    student1 = Student("Ram")
    student2 = Student("snehal")
    # print(Student.fetch_school_name())
    # print(student1.fetch_school_name())
    print(student1.school_name)
    print(student2.school_name)
    print(Student.school_name)
    student1.school_name = "student 1 school"
    print(student1.school_name)
    print(student2.school_name)
    print(Student.school_name)
    student2.school_name = "student 2 school"
    print(student1.school_name)
    print(student2.school_name)
    print(Student.school_name)




if __name__ =="__main__":
    main()