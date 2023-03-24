class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print("(person)person name is:", self.name)

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def print_student_id(self):
        print("(student)student id is:", self.student_id)

    def print_age(self):
        print("(student)student age is:", self.age)

def main():
    student = Student("ram", 24, 123)
    student.print_student_id()
    student.print_age()
    student.print_name()

if __name__ =="__main__":
    main()