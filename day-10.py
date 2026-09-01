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
'''