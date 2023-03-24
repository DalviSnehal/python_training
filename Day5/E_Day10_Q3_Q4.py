# Write classes linked through multiple inheritance but make sure their MRO throws an error
class A:
    def print_method(self):
        print("This is A:")


class B:
    def print_method(self):
        print("This is B:")


class C(A, B):
    pass


def main():
    c = C()
    c.print_method()
    print(C.mro())


if __name__ == "__main__":
    main()

