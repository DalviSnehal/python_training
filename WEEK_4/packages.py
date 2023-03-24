# from newpkg import mod1, mod2 as mod3
# form newpkg.mod2 import mod2_function
# print(mod1.mod1_func())
# mod3.mod2_function()

import newpkg

from newpkg.mod1 import *

newpkg.mod1.mod1_func()
newpkg.mod2.mod2_function()


import math
print(math.pi)
print(pi)

from math import pi
print(math.__file__)
print(newpkg.mod1.__file__)