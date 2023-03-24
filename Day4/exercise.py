# Create 2 classes Student (properties: age, name,
# subjects[list], marks[list]) and Exams( properties: subjects[list], pass_marks:[list] ) and override the __mul_
# _ method in Student and Exams such that if the values in each index of  marks in Student are greater than values in each index
# of pass_marks in Exams then return Pass else Fail

class Student:
    def __init__(self, age, name, subjects=["maths","science"], marks=[90, 45]):
        self.age =age
        self.name = name
        self.subjects = subjects
        self.marks = marks

    def __mul__(self,other):
        for idx, subject in enumerate(self.marks):
            if(self.marks[idx]>other.pass_marks[idx]):
                continue
