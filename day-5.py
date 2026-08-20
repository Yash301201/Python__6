''' 
# input()
# input() is used to take input from the user.
# By default, input() always gives the value as a string.

num = input("Enter a number : ")
print(num)


# split()
# split() is a string method.
# It divides a string into separate values.
# By default, it splits the string based on spaces.

numbers = input().split()
print(numbers)


# split(",")
# We can give a separator inside split().
# Here, "," means split the input wherever a comma is found.

num = input().split(",")
print(num)


# eval()
# eval() evaluates the input as a Python expression.
# It can convert input such as [1, 2, 3] into an actual list.
# It can also convert (1, 2, 3) into a tuple.
# Note: eval() should be used carefully because it can execute Python code.

num = eval(input("Enter : "))
print(num)


# Normal string formatting using comma
# We can print multiple values using commas.
# Python automatically adds a space between the values.

num = "Yash"
n_um = 24

print("My name is", num, "my age is", n_um)


# f-string
# f-string means formatted string.
# The letter 'f' means formatted.
# We can directly put variables inside {}.

print(f"My name is {num} and age is {n_um}")


# map()
# map() applies a function to every value.
# Here, str means convert every input value into a string.
# split(",") separates the input using commas.
# list() converts the map result into a list.

num = list(map(str, input().split(",")))
print(num)


# % formatting
# %s is used for a string.
# %d is used for an integer.
# The values are given after % inside parentheses.

print("My name is %s and %d" % (num, n_um))

'''