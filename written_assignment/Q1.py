# Write a basic class as an
# example containing 2 class variables, 3 instance variables and relevant getter and setter methods for
# the inatance variables.

class Student:
    #class variables
    school_name = "abc school"
    school_class = "msc"
    def __init__(self, id, age, name):
        self.name = name
        self.age = age
        self.id = id

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_id(self, id):
        self.id = id
        # return "set successfully"
    def set_age(self, age):
        self.age = age
        # return "set successfully"
    def set_name(self, name):
        self.name = name
        # return "set successfully"

def main():
    student1 = Student(12, 23, "snehal")
    print("school_name:", student1.school_name, "class name:", student1.school_class, "student_id", student1.id, "student_name:", student1.name, "student_age:", student1.age)
    print(student1.get_id())
    student1.set_id(13)
    print(student1.get_id())
    print(student1.get_age())
    student1.set_age(24)
    print(student1.get_age())
    print(student1.get_name())
    student1.set_name("abhijeet")
    print(student1.get_name())
if __name__ =="__main__":
    main()
