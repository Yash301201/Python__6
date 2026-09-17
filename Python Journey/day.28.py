'''
for i in range(3):

    name = input("Enter your name: ")

    weight = float(input("Enter your weight in kg: "))

    unit = input("Enter height unit (feet/cm/inches/meters): ").lower()

    height = float(input("Enter your height: "))

    if unit == "feet" or unit == "feets":
        height_m = height * 0.3048

    elif unit == "cm":
        height_m = height / 100

    elif unit == "inches":
        height_m = height * 0.0254

    elif unit == "meters":
        height_m = height

    else:
        print("Invalid height unit")
        continue

    bmi = weight / (height_m ** 2)

    print("Name:", name)
    print("BMI:", round(bmi, 2))

    if bmi < 18.5:
        print("Underweight")

    elif bmi < 25:
        print("Normal weight")

    elif bmi < 30:
        print("Overweight")

    else:
        print("Obesity")

    print("------------------")

    n = []
w = []
h= []
for i in range(5):
    name = input()
    n.append(name)
    weight = float(input())
    w.append(weight)
    height = float(input())
    h.append(height)
print(n)
print(w)
print(h)
#Store  the name, weight, height, in a dictionary/list
#In this case we want 5 iterations to be happened 
dict_ = {'n' : [],
         'w' : [],
         'h' : []
}
n_ = int(input())
for i in range(n_):
    name = input()
    dict_['n'].append(name)
    weight = float(input())
    dict_['w'].append(weight)
    height = float(input())
    dict_['h'].append(height)
print(dict_['n'])
print(dict_['w'])
print(dict_['h'])
'''
#Exception handling-->
#Exception Handling is a mechanism to a program which responds to run time 
#error or compilations
#Exception --> Tis tries to make out programm go in a normal flow
'''
try, except, finally
for every try except is mandaotory
try:
    #code that may cause an error....
    .....
except:
    #code that handle the error 
    .....
finally:
    .....
    ......

a,b = map(int,input("Enter value: ").split(','))
try:
    result = a/b
    print(result)
except Exception as e:
    print('Find it')

#simple scenario to understand the exception

try:
    a,b = map(int,input("Enter value: ").split(','))
    result = a/b
    print(result)
except Exception as e:
    print('Find it')
    print(e)
#In above case we will get ValueError , ZeroDivisionError
#Possible types of errors --> TypeError, ValueError, NameError,
#IndexError,ZeroDivisionError,AttributeError,ArithmeticError.....

try:
    a,b = map(int,input("Enter value: ").split(','))
    result = a/b
    print(result)
except ValueError:
    print('Enter the intergers carefully')
    print(ValueError)
except ZeroDivisionError:
    print("Make sure to give denominator greater than zero")
except NameError:
    print("Please first understand the syntax and be good at spelling")
except AttributeError:
    print("Carefully check the methods")
finally:
    print("It's done now you understand exception handling!")
'''
try:
    a = [12,5,4,7]
    print(a[5])
    a.append('codegnan')
    print(a)
except (IndexError, NameError, AttributeError) as e:
    print(e)
finally:
    print("Done")