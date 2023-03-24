# What is Hybrid Inheritance? Write a code example showing how it works? What is MRO and write a
# code example showing where it can be used
class A:
    def print_method(self):
        print("This is A:")

class B(A):
    def print_method(self):
        print("This is B:")

class C(A):
    def print_method(self):
        print("This is C:")

class D(B, C):
    def print_method(self):
        print("This is D:")

def main():
    d = D()
    d.print_method()


if __name__ =="__main__":
    main()


class A:
    def print_method(self):
        print("This is A:")

class B(A):
    def print_method(self):
        print("This is B:")

class C(A):
    def print_method(self):
        print("This is C:")

class D(B, C):
    def print_method(self):
        print("This is D:")

def main():
    d = D()
    d.print_method()
    print(D.mro())

if "__main__" == __name__:
    main()