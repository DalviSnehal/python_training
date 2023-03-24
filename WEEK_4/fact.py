import sys


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv)
        print(fact(int(sys.argv[1])))
    else:
        print(fact(5))
