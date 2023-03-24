class Student:
    school_name = "ABC School"

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


    @classmethod
    def __change_school_name(cls, school_name):
        cls.school_name = school_name

    def __print_student_details(self):
        print(self.name)

class CollegeStudent(Student):
    school_name = "DEF School"

    def __init__(self, college_id, student_id, name):
        super().__init__(name, student_id)
        self.college_id = college_id


    def __print_student_details(self, some_str):
        print(self.name, self.college_id, some_str)


def main():
    student = Student("ram", 1234)
    college_student = CollegeStudent(1234, 2345, "shyam")
    # college_student.print_student_details()
    print(CollegeStudent.school_name)
    # CollegeStudent.__change_school_name("FGH School")
    # print(student._Student__student_id)
    # student._Student__print_student_details()
    # college_student._CollegeStudent__print_student_details()
    college_student._CollegeStudent__print_student_details("some string")
if __name__ =="__main__":
    main()