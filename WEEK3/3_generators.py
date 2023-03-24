import cProfile
import sys


def inf_seq():
    num = 0
    while True:
        if num % 47 == 0:
            print("Inside if", num)
            i = (yield num)
            if i is not None:
                print("i = ", i)
                num = i
            else:
                print("i: None")
        num = num + 1
        # print(num)


def finite_seq():
    num = 1
    while True:
        return num
    num = num + 1


def yield_example():
    str1 = "This is the first yield"
    yield str1
    str2 = "This is the second yield"
    yield str2
    str3 = "This is the third yield"
    yield str3


def main():
    my_lst = [i for i in range(1, 6)]
    print(my_lst)

    # print(finite_seq())
    """
    # for num in inf_seq():
    #     print(num)
    #
    # gen_obj = inf_seq()
    # print(next(gen_obj))
    # print(next(gen_obj))
    # print(next(gen_obj))
    # print(next(gen_obj))
    # print(next(gen_obj))

    lst_comp = [i for i in range(1, 10000)]
    gen_comp = (i for i in range(1, 10000))

    print(sys.getsizeof(lst_comp))
    print(sys.getsizeof(gen_comp))

    cProfile.run("sum([i for i in range(1, 10000)])")
    cProfile.run("sum((i for i in range(1, 10000)))")

    gen_obj = yield_example()
    print(next(gen_obj))
    print(next(gen_obj))
    print(next(gen_obj))
"""  # print(next(gen_obj))
    inf_obj = inf_seq()
    num = inf_obj.send(None)
    while True:
        print("The num divisible by 47 is: ", num)
        num = inf_obj.send(num * 10)
        print("num: ", num)
        if num > 10000:
            inf_obj.close()
            break


if __name__ == "__main__":
    main()
