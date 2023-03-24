class Student:
    school_name = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school_name(cls, school_name):
        cls.school_name = school_name

class CollegeStudent(Student):
    college_name = "DEF School"

    def __init__(self, college_id, name):
        super().__init__(name)
        self.college_id = college_id

def main():
    student = Student("snehal")
    collegestudent = CollegeStudent(1234, "abhi")
    print(CollegeStudent.school_name)
    CollegeStudent.change_school_name("FGH School")
    print(CollegeStudent.school_name)
    print(Student.school_name)
if __name__ =="__main__":
    main()