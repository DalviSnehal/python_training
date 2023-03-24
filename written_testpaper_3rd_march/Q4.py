# 4. Describe multiple inheritance? Write a code example demonstrating how multiple inheritance workS

class Mammal:
    def __init__(self, species_type, num_of_legs, food_type):
        self.species_type = species_type
        self.num_of_legs = num_of_legs
        self.food_type = food_type

    def describe_mammal(self):
        print("mammal attributes are:", self.species_type, self.num_of_legs, self.food_type)

    def can_walk(self):
        return True


class Human:
    def __init__(self, can_think, qualification):
        self.can_think = can_think
        self.qualification = qualification

    def describe_human(self):
        print("human attributes are:", self.can_think, self.qualification)

    def can_speak(self):
        return True

class Student(Human, Mammal):
    def __init__(self, species_type, num_of_legs, food_type, can_think, qualification):
        Human.__init__(self, can_think, qualification)
        Mammal.__init__(self, species_type, num_of_legs, food_type)

def main():
    student = Student("Mammal", 2, "Omni", True, ["HIGH SCHOOL"])
    print(student.can_speak())
    student.describe_human()
    student.describe_mammal()
    print(student.can_walk())
if __name__ == "__main__":
    main()
