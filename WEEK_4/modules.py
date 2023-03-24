"""
import mod
import sys

print(mod.my_lst)

print(mod.my_string)

print(mod.my_function())

print(sys.path)

"""
import sys

# sys.path.append(r'C:\\Users\\Lenovo\\PycharmProjects\\pythontraining\\WEEK_4')

# import mod2

# System Path (Windows Env variables), Python Installed directories
# same directory
# import mod
# import re
# import math
#
# print(mod.__name__, mod.__file__)
# print(re.__name__, re.__file__)
# print(math.__name__, math.__file__)
#
# print(math.pi)
# import mod
# from mod import my_lst, my_function
# from mod import *
# from mod import my_lst as some_lst
# print(some_lst)
#
# my_function()

def main():
    import math
    print(math.pi)
    # from math import * ->not correct
    # from math import pi ->this is okay

try:
    import mod2
except ModuleNotFoundError as me:
    print(me)

print(dir())
import mod
print(dir())

mod.my_lst.append(5)
print(mod.my_lst)
#
# from mod import my_lst
# print(dir())


import mod

import importlib
importlib.reload(mod)