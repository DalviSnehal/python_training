class Employee:
    def __init__(self, name, age, _id, salary_per_hour):
        self.name = name
        self.age = age
        self.id = _id
        self.salary_per_hour = salary_per_hour

    def get_salary_per_hour(self):
        return self.salary_per_hour

class Timesheet:
    def __init__(self, _id, hours):
        self.id = _id
        self.hours = hours

    def get_hours(self):
        return self.hours

    def __mul__(self, other):
        return self.get_hours() * other.get_salary_per_hour()

def main():
    emp = Employee("Ram", 22, 1234, 10)
    timesheet = Timesheet("1234", 10)
    print(timesheet * emp)
#
# def __mul__(self,other):
#     return self.get_hours() * other.get_salary_per_hour()



if __name__ =="__main__":
    main()