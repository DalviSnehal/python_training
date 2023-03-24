# 1. What is inheritance in Python? What are the different types of inheritance? Write an example code
# snippet for Single Inheritance and Multilevel Inheritance


# # single inheritance
# class Parent:
#     def __init__(self, sir_name):
#         self.sir_name = sir_name
#
#     def print_parent_information(self):
#         print("parent information is:", self.sir_name)
#
# class Child(Parent):
#     def __init__(self,sir_name, name):
#         super().__init__(sir_name)
#         self.name = name
#
#     def print_child_information(self):
#         print("child information is:",self.sir_name, self.name)
#
# def main():
#     child = Child("dalvi", "snehal")
#     child.print_child_information()
#     child.print_parent_information()

class GrandFather:
    def __init__(self, grand_fathername):
        self.grand_fathername = grand_fathername

class Father(GrandFather):
    def __init__(self, grand_fathername, father_name):
        super().__init__(grand_fathername)
        self.fathername = father_name

class  Son(Father):
    def __init__(self, father_name, grand_fathername, sonname):
        super().__init__(father_name, grand_fathername)
        self.sonname = sonname

    def print_name(self):
        print('Grandfather name :', self.grand_fathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)


def main():
    s1 = Son("satish", "ashish", "ram")
    print(s1.grand_fathername)
    s1.print_name()
if __name__ == "__main__":
    main()