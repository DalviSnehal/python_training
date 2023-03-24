from multipledispatch import dispatch

@dispatch(int, int)
def add(a, b):
    return a + b




@dispatch(int, int, int)
def add(a, b, c):
    return a + b + c


@dispatch(float, float)
def add(a, b):
    return a + b

def main():
    print(add(1, 2, 3))
    print(add(1.1, 2.2))
    print(add(1, 2))




if __name__ =="__main__":
    main()