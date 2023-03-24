# Define any class of your choice and use these keywords to introspect your object: dir, id, type, hasattr(), getattr(), __repr__, __doc__, __name__

class Student:
    """

    this is for student class.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_student_attributes(self):
        print("student attributes are:", self.name, self.age)

    def __repr__(self):
        return "Student attributes Repr:" + self.name + str(self.age)


def main():
    student1 = Student("snehal", 17)
    student2 = Student("Abhi", 18)
    print(dir(student1))
    print(id(student2))
    print(type(student1))
    print(Student.__doc__)
    print(Student.__name__)
    print(hasattr(student1, "print_student_attributes"))
    print(getattr(student1, "name"))
    print(repr(student2))
    student1.print_student_attributes()


if __name__ == "__main__":
    main()
