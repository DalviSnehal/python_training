# Write a Python program to triple all numbers in a given list of integers, use map.
# my_lst = [1, 2, 3, 4, 5, 6]
# changed_lst = []
# for i in my_lst:
#     changed_lst.append((i*3))
# print(changed_lst)
# print(list(map(lambda x: x*3, my_lst)))


# Write a Python program to add three given lists using Python map and lambda
"""
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]

print(list(map(lambda x1,x2, x3: x1 + x2 + x3, lst1, lst2, lst3)))
"""
from audioop import avg
from functools import reduce

# Write a Python program to convert a given list of integers into a list of strings. Use map and lambda
"""
list_int = [1, 12, 15, 21, 131]
list_string = map(str, list_int)
print(list(list_string))
print(list(map(lambda x : str(x), list_int)))
"""

# Using the filter function, filter the even numbers so that only odd numbers are passed to the new list.
"""
a = []
for i in range(1, 101):
    a.append(i)
print(list(filter(lambda x: x % 2 == 1, a)))
"""

# Using filter() function filter the list so that only negative numbers are left.
"""
lst = [1 ,2, -1, -2, -3, -5]
print(list(filter(lambda x : x < 0, lst)))
"""

# Using filter() and list() functions and .lower() method filter all the vowels in a given string str = \
# "Winter Olympics in 2022 will take place in Beijing China”


str_1 = "Winter Olympics in 2022 will take place in Beijing China"
# vowels = ['a', 'e', 'i', 'o', 'u']
# print(list(filter(lambda x: x in str_1, vowels)))
print(list(filter(lambda x: True if x.lower() in "aeiou" else False, str_1)))

# Using map() and filter() functions add 2000 to the values below 8000
lst1 = [1000, 500, 600, 700, 5000, 90000, 17500]
print(list(map(lambda x: x + 2000, filter(lambda x: x < 8000, lst1))))

# Use reduce to find the average of all numbers in a list
"""
from functools import reduce

inp_lst = [1, 2, 5, 9]
lst_len= len(inp_lst)
print("avg of given list", inp_lst, "is", )
print(reduce(lambda x, y: x + y, inp_lst) /lst_len)
"""
# Find the max number in a list using reduce
"""
from functools import reduce

list1 = [5, 67, 90, 100, 500, 2, 3, 1000, 50, 40]
print(reduce(lambda x, y: x if x > y else y, list1))
"""
# Filter only negative and zero in the list using list comprehension
"""
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([num for num in numbers if num < 0])
print([num for num in numbers if num == 0])
"""

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]# output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print([item for sublist in list_of_lists for item in sublist])