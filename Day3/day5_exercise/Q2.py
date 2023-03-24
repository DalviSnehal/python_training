"""
Choose any class of your liking and write 2 instance variable, 1 class variable, and write one
class method that can change the value of that class variable and one class method that can
display the value of that class variable, write a static method that does not utilise either the class
variable or the instance variable.
"""
class Teacher:
    teacher_name = "xyz"

    def __init__(self, age, name):
        self.name = name
        self.age = age

    @classmethod
    def change_teacher_name(cls, teacher_name):
        cls.teacher_name = teacher_name

    @classmethod
    def fetch_teacher_name(cls):
        return cls. teacher_name

    @staticmethod
    def get_name(role):
        return role




def main():
    teacher = Teacher(25, "ajay")
    print(teacher.teacher_name)
    print(Teacher.teacher_name)
    teacher.teacher_name = "abc"
    print(teacher.teacher_name)
    print(Teacher.teacher_name)


if __name__ == "__main__":
    main()




if __name__ =="__main__":
    main()