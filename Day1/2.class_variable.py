
class Student:
    school_name="Saraswati Vidya Mandir"
    # this is class variable and it is access also by using class name or object name

    def __init__(self, name, age):
        self.name=name
        self.age=age  #this are the instance  variables

def  main():
    student1=Student("Ram", 17)
    student2=Student("Shyam", 15)
    print(student1.age, student1.name)
    print(student2.age, student2.name)
    print(student1.school_name, student2.school_name, Student.school_name)











if __name__ =="__main__":
    main()