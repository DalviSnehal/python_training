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