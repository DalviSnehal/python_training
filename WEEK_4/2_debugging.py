import pdb

def perform_division(a, b):
    print(a, b)
    return a/b

def perform_mul(a, b):
    return a * b

def main():
    pdb.set_trace()
    a = 1
    b = 1
    perform_division(a, b)
    perform_mul(a, b)

    for i in range(5):
        print(i)

if __name__ == "__main__":
    main()