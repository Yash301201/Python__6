'''
Function : A function is a block of code that can be executed when called. 
It allows for code reusability and better organization.
Functions can take inputs, known as parameters, and can return outputs. They are defined using the 'def' keyword in Python, followed by the function name and parentheses. Inside the parentheses, you can specify any parameters the function may need. The code block within the function is indented.

syntax: 
def function_name(parameters):
    pass  # This is a placeholder for the function body
function_name(arguments)  # This is how you call the function
    
example:
def add_numbers(num1, num2):
    return num1 + num2
add_numbers(5, 10)  # This will return 15
print(add_numbers(5, 10))  # Output: 15

Arguments:
Arguments are the actual values you pass to a function when calling it.
They correspond to the parameters defined in the function.
Arguments can be of any data type, including numbers, strings, lists, or even other functions.
Positional arguments are passed in the order they are defined, while keyword arguments are passed by explicitly naming them.(same as parameters should be same as arguments)

Syntax:
def function_name(arguments):
    pass  # This is a placeholder for the function body
function_name(arguments)  # This is how you call the function

Default Arguments:
Default arguments are values assigned to parameters in the function definition. If no argument is passed for a default parameter, the default value is used.
Example:
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", "Hi"))  # Output: Hi, Bob!

Example of function with default arguments:
def data(a=8,b=6):
    print(a+b)
data(1,3)  # Output: 4
data()  # Output: 14

Keyword Arguments:
Keyword arguments are passed to a function by explicitly naming the parameter and providing a value.
This allows you to pass arguments in any order, as long as the parameter names are specified.

example-1:
def introduce(name, age):
    return f"Hello, I'm {name} and I'm {age} years old."
print(introduce(name="Yash", age=25))  # Output: Hello, I'm Yash and I'm 25 years old.
print(introduce(age=30, name="Mahesh"))  # Output: Hello, I'm Mahesh and I'm 30 years old.

example-2:
def data(name, age,batch,location):
    print(f"Name: {name}, Age: {age}, Batch: {batch}, Location: {location}")
data(name="Yash", age=25, batch="Python", location="India")
output: Name: Yash, Age: 25, Batch: Python, Location: India

example-3:
def all(*name):
    print(name[1])
all("Yash", "Mahesh", "Ramesh")  # Output: Mahesh

example-4:
def all(*name):
    print(name)
all("Yash", "Mahesh", "Ramesh")  # Output: ('Yash', 'Mahesh', 'Ramesh')

Varibale-length Arguments:
Variable-length arguments allow you to pass a variable number of arguments to a function. In Python, you can use the *args syntax to accept any number of positional arguments, and **kwargs to accept any number of keyword arguments.
example-1:
def sum_numbers(*args):
    return sum(args)
sum_numbers(1, 2, 3, 4)  # Output: 10

Keyword-only Arguments:
Arguments that can only be passed as keywords, not as positional arguments.
example:
def display_info(**, name, age):
    print(f"Name: {name}, Age: {age}")
display_info(name="Yash", age=25)  # Output: Name: Yash, Age: 25

return keyword:
The return keyword is used in a function to send a value back to the caller. 
When a function reaches a return statement, it exits the function and returns the specified value.
If no return statement is encountered, the function returns None by default.

example:
def multiply(a, b):
    return a * b
result = multiply(5, 3)  # result will be 15
print(result) 

Passing by reference: 
scope of variable: 
1.Local varibles: A varibale is define inside the function call it as local varible, 
where the variable can only access with in that function
()--> parentheses 
examples: 
def display():
    name = "Yash"
    print(name)
display() 


2.Global varibles: A variable is defined outside of any function, making it accessible throughout the entire program.
examples:   
a = 90 ---> global variable
def display():
    print(a)
display()
print(a)

global keyword: The global keyword is used to declare that a variable inside a function is global,
allowing you to modify the global variable from within the function.
(Globl is a keyword used to re-assign new values to varibles that was already define outside of the function call)
example:
def update_global():
    global a
    a = 100  # This modifies the global variable 'a'
    a = 90
update_global()
print(a)  # Output: 90

passing by value: 

def eve_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
eve_odd(4)  # Output: "Even"
print(eve_odd(4))  # Output: Even (passing by value)

passing by reference:
example : 
def modify_list(lst):
    lst.append(4)  # This modifies the original list
my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4] (passing by reference)

example-2:
num = 4
def eve_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
eve_odd(4)  # Output: "Even"
print(eve_odd(num))  # Output: Even (passing by value)

Recursive functions:
A recursive function is a function that calls itself in order to solve a problem.
syntax:
def recursive_function(parameters):
    if base_condition:
        return base_value
    else:
        return recursive_function(modified_parameters)

example:
def factorial(n):
    if n == 0 or n == 1:  # Base condition
        return n
    else:
        return n * factorial(n - 1)  # Recursive call
print(factorial(5))  # Output: 120

lambda functions:
Lambda functions are anonymous functions defined using the 'lambda' keyword. They can take any number of
arguments but can only have one expression.
example:
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8
example-2:
greater = lambda a, b: a if a > b else b
print(greater(10, 20))  # Output: 20

example-3:
greater = lambda num1, num2: num1 if num1 > num2 else num2
print(greater(15, 25))  # Output: 25

example-4:
even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(even_odd(4))  # Output: Even

example-5:
cube = lambda x: x ** 3
print(cube(3))  # Output: 27

filter() function:
The filter() function is used to filter elements from an iterable based on a specified condition.
It returns an iterator containing only the elements that satisfy the condition.
(filter() checks each item and keeps only the items we want.)
syntax:
filter(function, iterable)

example:
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]

map() function:
The map() function applies a specified function to each item in an iterable (like a list)
and returns an iterator with the results.(The map() function applies the same function to every item in a list and gives the results.)
syntax:
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

reduce() function:
Take multiple values and keep combining them until only ONE value is left.
functools is a Python module. reduce() combines multiple values step by step and gives one final value.
syntax:
numbers = [1, 2, 3, 4, 5]
from functools import reduce
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)  # Output: 15

numbers = [1, 2, 3, 4, 5]
from functools import reduce
sum_numbers = reduce(lambda x, y: x + y, range(1, 10))
print(sum_numbers) #output: 45

List Comprehension:
List comprehension is a concise way to create lists in Python.
It allows you to generate a new list by applying an expression to each item in an existing iterable,
optionally filtering items based on a condition.(List comprehension is a simple and short way to create a new list from an existing list.)

syntax:
new_list = [expression for item in iterable if condition]
example:
squared_numbers = [x ** 2 for x in range(1, 10) if x % 2 == 0]
print(squared_numbers)  # Output: [4, 16, 36, 64] 

example-2:
any = [[i * j for j in range(1, 11)] for i in range(1, 11)]
print(any) # nested list comprehension

example-3:
of = [[1,2,3],[4,5,6],[7,8,9]]
lst = [i for j in of for i in j]
print(lst)

Set Comprehension:
Set comprehension is similar to list comprehension, but it creates a set instead of a list.
syntax:
new_set = {expression for item in iterable if condition}
example:
squared_numbers_set = {x ** 2 for x in range(1, 10) if x % 2 == 0}
print(squared_numbers_set)  # Output: {64, 4, 36, 16} (Note: Sets are unordered, so the output may vary in order)


Generator :
A generator is a special type of iterator in Python that allows you to iterate over a sequence of values without storing the entire sequence in memory.
Generators are defined using functions and the 'yield' keyword.
When a generator function is called, it returns a generator object, which can be iterated over to produce values one at a time.

example:
def all_():
    for i in range(1, 6):
        yield i  # Yielding values one at a time
i = all_()  # Creating a generator object
print(next(i))  # Output: 1

importing modules: 
To use functions, classes, or variables defined in another Python file (module),
you can import that module into your current script using the 'import' statement.
This allows you to access and utilize the code from the imported module.
syntax: import module_name
example:
import math
print(math.sqrt(16))  # Output: 4.0

example-2:
import random
print(random.randint(1, 10))  # Output: A random integer between 1 and 10

example-3:
import python_module
python_module.greet("Alice")  # Output: Hello, Alice!

User-defined modules:
You can create your own Python modules by defining functions, classes, or variables in a separate .py file.
To use your user-defined module, you can import it into another Python script using the 'import' statement.
example: 
import my_module
my_module.my_function()  # Calling a function from the user-defined module

example-2:
from my_module import my_function
my_function()  # Calling the imported function from the user-defined module 

example-3:
from newfile import add, sub, mul
print(add(5, 3))  # Output: 8
print(sub(10, 4))  # Output: 6
print(mul(2, 7))  # Output: 14

example-4:
import newfile as nf
print(nf.add(5, 3))  # Output: 8


built-in modules:
Python provides a wide range of built-in modules that offer various functionalities,
such as math operations, file handling, data manipulation, and more.
You can import and use these modules in your Python programs without the need for external installations.
examples: os, sys, math, random, datetime, json, re, itertools, functools, collections, and many more.
import os (To communicate with the operating system)
print(os.getcwd())  # Output: /your/current/directory (current working directory)

example-2:
import sys (To access system-specific parameters and functions)
print(sys.version)  # Output: 3.8.5 (or your current Python version)

example-3:
import datetime (To work with dates and times)
print(datetime.datetime.now())  # Output: 2026-09-05 14:27:17.550060 (current date and time)

example-4:
import random (To generate random numbers)
print(random.randint(1, 100))  # Output: A random integer between 1 and 100

example-5:
import smtplib
print("Welcome to the email sender program!")
'''
