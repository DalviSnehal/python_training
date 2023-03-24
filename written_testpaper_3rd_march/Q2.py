# . What is overriding in Python? Describe it and write a code example demonstrating how overriding is
# working.

class GF:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("parent name is:", self.name)

class Father(GF):
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("father_name is", self.name)

def main():
    gf = GF("Dattatray")
    gf.print_name()
    father = Father("Satish")
    father.print_name()

if __name__ == "__main__":
    main()