class Student:
    school_name = "DEF school"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school_name(cls, school_name):
        cls.school_name = school_name

def main():
    # del Student.change_school_name
    # delattr(Student, "change_school_name")
    Student.change_school_name("ABCD school")




if __name__ =="__main__":
    main()