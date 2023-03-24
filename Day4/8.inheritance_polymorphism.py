class Student:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("Student:", self.name)


class CollegeStudent(Student):
    def __init__(self, name):
        super().__init__(name)

    def print_name(self):
        print("College Student:", self.name)


def main():
    student = Student("Rama")
    college_student = CollegeStudent("Shyama")
    student.print_name()
    college_student.print_name()

if __name__ == "__main__":
    main()
