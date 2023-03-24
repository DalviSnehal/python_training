from functools import reduce


def function_one():
    print("I am function one")


def function_two():
    return function_one


def function_three(x):
    return x, x ** 2, x ** 3


def function_four(x):
    return abs(x)


def function_five(a, b, c):
    return a + b + c


def function_six(x):
    if x % 2 == 0:
        return False
    return True


def function_seven(a, b):
    return a + b


def main():
    """ another_name = function_one
    another_name()
    my_list = [1, "string", function_one]
    my_list[2]()
    print(function_one)
    # function composition
    (function_two())()

    my_list_2 = ["ram", "rohit", "ansari", "aman", "surabhi"]
    print(sorted(my_list_2))
    print(sorted(my_list_2, key = len))
"""
    # lamda
    lambda_ex = (lambda x: x ** 2)
    print(lambda_ex(5))
    print((lambda x: x + 10)(90))

    my_list_2 = ["ram", "rohit", "ansari", "aman", "surabhi"]
    print(sorted(my_list_2, key=lambda x: -len(x)))

    # multiple values
    print(function_three(3))

    lambda_multiple = (lambda x: [x, x ** 2, x ** 3])
    print(lambda_multiple(4))

    lambda_multiple = (lambda x: (x, x ** 2, x ** 3))
    print(lambda_multiple(4))

    # map : map(function/operation, List/iterable)
    my_list_3 = [1, -4, 7, -10, 101, -123]
    map_obj = map(function_four, my_list_3)
    map_lambda_obj = map(lambda x: abs(x), my_list_3)
    print("lambda method abs:", list(map_lambda_obj))
    for item in map_obj:
        print(item)

    map_output = list(map(function_four, my_list_3))
    print(map_output)

    #  multiple iterables
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    list3 = [11, 12, 13, 14, 15]
    print(map(function_five, list1, list2, list3))
    print(list(map(lambda x1, x2, x3: x1 + x2 + x3, list1, list2, list3)))

    # filter
    list4 = []
    for i in range(1, 101, 1):
        list4.append(i)
    # print(list4)
    print(list(filter(function_six, list4)))
    print(list(filter(lambda x: x % 2 == 1, list4)))

    # reduce
    list5 = []
    for i in range(1, 11, 1):
        list5.append(i)
    print(list5)
    print(reduce(function_seven, list5))
    print((reduce(function_seven, list5), 10))
    print(reduce(lambda a, b: a + b, list5))
    print("list 5 is", list5)
    print(sum(list5))
    # list comprehension
    list6 = []
    for i in range(1, 51, 1):
        list6.append(i)
    print(list6)
    list7 = [itr for itr in range(1, 51, 1)]
    list8 = [i + j for i in range(1, 10) for j in range(1, 10) if i == j]
    print(list8)

    # dictionary comprehension
    my_dict = {i: i ** 3 for i in range(1, 10) if i % 2 == 0}
    print(my_dict)

    # set comprehension
    duplicates_list = [1, 2, 3, 4, 4, 5, 5, 5]
    my_set = {i for i in duplicates_list if i % 2 == 1}
    print(my_set)

    my_tuple = (i for i in range(1, 10))
    for i in my_tuple:
        print(i)
    # print(my_tuple)


if __name__ == "__main__":
    main()
