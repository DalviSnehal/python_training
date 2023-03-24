class Student:#constructor with default values

    def __init__(self, name, age=17):
        self.age=age
        self.name=name

    def print_student_details(self):
        print("this is for the student details:", self.name, self.age)


def main():
    student=Student("Ram", 20)
    student.print_student_details()






if __name__ =="__main__":
    main()