class A:
    def print_method(self):
        print("This is A:")


class B(A):
    def print_method(self):
        print("This is B:")


class C(B):
    pass


def main():
    c = C()
    c.print_method()
    print(C.mro())


if __name__ == "__main__":
    main()
