# Write a generator that generates prime numbers in the range 1 to 5000


def prime_fun():
    for number in range(1, 5000 + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                yield number


def main():
    for num in prime_fun():
        print(num)


#
# def main():
#     # for num in getPrimes(5000):
#     #     print(num)
#     #
#     # gen_obj = getPrimes(5000)
#     # print(next(gen_obj))
#     getPrimes(500)
#



if __name__ == "__main__":
    main()
