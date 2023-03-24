# Write classes linked through multiple inheritance and print their MRO

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_attributes(self):
        print("student attributes are:", self.name, self.age)


class Teacher:
    def __init__(self, qualification, id):
        self.qualification = qualification
        self.id = id

    def print_teacher_attributes(self):
        print("teacher attributes are:", self.qualification, self.id)


class University(Student, Teacher):
    def __init__(self, name, age, qualification, id):
        Student.__init__(self, name, age)
        Teacher.__init__(self, qualification, id)

def main():
    university = University("snehal", 24, "Engineer", 213)
    university.print_teacher_attributes()
    print(University.mro())
    university.print_attributes()
    print(University.mro())

if __name__ == "__main__":
    main()