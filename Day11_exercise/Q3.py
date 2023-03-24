# Create 3 classes in which 2 are parent child and 1 is completely different and utilise the is
# isinstance and issubclass keywords to show  their usage.

class Parent:
    def __init__(self, name, sir_name):
        self.name = name
        self.sir_name = sir_name

class Child(Parent):
    def __init__(self, name, sir_name, age):
        super().__init__(name, sir_name)
        self.age = age

class Person:
    def __init__(self, height):
        self.height = height


def main():
    parent = Parent("xyz", "abc")
    child = Child("abc", "xyz", 17)
    person = Person(5.5)
    print(issubclass(Parent, Child))
    print(issubclass(Child, Parent))
    print(issubclass(Person, Parent))
    print(issubclass(Parent, Person))
    print(issubclass(Child, Person))
    print(issubclass(Person, Child))
    print(isinstance(person, Child))
    print(isinstance(child, Child))
    print(isinstance(person, Person))

if __name__ == "__main__":
    main()