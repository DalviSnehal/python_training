# Types of Exceptions
def main():
    # syntax error
    # print 'hello world'  ->print("hello world")
    # name error
    # print(name)
    name = "ram"
    print(name)
    # indexerror
    my_lst = [1, 2, 3, 4, 5]
    # print(my_lst[7]) ->print(my_lst[0], my_lst[4])
    # modulenotfounderror
    # import maths  ->import math
    # AttributeError
    import math
    # print(math.PI)
    print(math.pi)
    # KeyError
    person_data = {'name' : 'Ram', 'country' : 'India'}
    # print(person_data['county']) ->
    print(person_data['country'])
    # TypeError
    # from math import power
    # from math import pow
    # ValueError
    # print(int('12z'))
    # ZeroDivisionError
    my_lst = [1, 0]
    # print(1/0)
    # print(num/my_lst[1])

if __name__ =="__main__":
    main()