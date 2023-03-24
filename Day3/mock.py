class Employee:
    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary


def main():
    emp1 = Employee(123, "snehal", 12000, "cs")
    print(emp1.id, emp1.name, emp1.salary, emp1.department)
    print(emp1.get_salary())
    emp1.set_salary(18000)
    print(emp1.get_salary())


if __name__ == "__main__":
    main()
