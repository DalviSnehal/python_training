# Create a short program that prompts the user for a list of
# grades separated by commas. Split the string into individual grades
# and use a list comprehension to convert each string to an integer.
# You should use a try statement to inform the user when the values they entered cannot be converted.

grades = input("Please enter your grades, separated by commas: ").split(",")
print(grades)
try:
    grades = [int(grade) for grade in grades]
    print(grades)
except ValueError:
    print("The grades you entered were in an invalid format.")

print(int('12'))