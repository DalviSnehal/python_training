def function_one():
    return "This is function one"


def function_two():
    def function_three():
        return "This is function three"

    return function_three


def function_four():
    string = "This is func four"

    def function_five():
        return string + " " + "and function five."

    return function_five


def convert_to_upper(function):  # closure
    def inner_logic():
        func = function()
        updated_func_val = func.upper()
        return updated_func_val

    return inner_logic


def split_the_string(function):
    def inner_logic():
        func = function()
        updated_fun_val = func.split()
        return updated_fun_val

    return inner_logic


@split_the_string
@convert_to_upper
def hello_world():
    return "Hello to the World"


def main():
    """
    f1 = function_one
    print(f1())
    f2 = function_two()
    print(f2())
    f4 = function_four()
    print(f4())"""
    print(hello_world())


if __name__ == "__main__":
    main()
