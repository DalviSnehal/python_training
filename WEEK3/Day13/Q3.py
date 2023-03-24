# 3. Write a decorator called printer which causes any decorated function to print their return values.
# If the return value of a given function is None, printer should do nothing

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