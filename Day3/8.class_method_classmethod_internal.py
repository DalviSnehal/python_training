class Student:
    school_name = "DEF school"

    def __init__(self, name):
        self.name = name

    def change_school_name(cls, school_name):
        cls.school_name = school_name

def main():
    student_obj = Student("Ram")
    Student.change_school_name(student_obj, "PQR school")
    # Student.change_school_name("Abc school", "FGH")
    Student.change_school_name = classmethod(Student.change_school_name)
    Student.change_school_name("ABC school")
    print(Student.school_name)
    print(student_obj.school_name)

if __name__ =="__main__":
    main()