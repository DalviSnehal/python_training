




# encapsulation is the mechanism of wrapping the data and methods that work on data within one unit
class Employee:
    def __init__(self, age, name):
        self.age = age
        self.name = name
# the above age and name are the data members
# below is the method
    def print_emp_data(self):
        print("emp information with name", self.name, "and age is", self.age)


# A good example of encapsulation could be when you go to a bank,
# and tell the banker(Object) to make a deposit(Method) of X dollars into your account(object), but to do so
# the banker request's you to give him your account number and the amount of cash you wish to deposit.


if __name__ =="__main__":
    main()