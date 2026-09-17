'''
input() --> input formatting 
print() --> output formatting (fstring)
a,b = 13,4.5
print(a,b)
print(a,b, sep = ',')
print(9,15, sep = ':')
print('codegnan','python','vizag',sep = '--->')
print(a,b,end = " ") # end by default throws new line, we can modify it..
print('codegnan is in vizag', end = '\t')
print('Hello Yash')#codegnan is in vizag     Hello Yash
ser1 = int(input())
user2 = int(input())
user3 = int(input())
user4 = int(input())
add = user1 + user2 + user3 + user4
sub_ = user1 - user2 - user3 - user4
mul = user1 * user2 * user3 * user4
div = user1 / user2
print(add,sub_,mul,div)
output:
10
5 
2
1
18 2 100 2.0
user1 = int(input())
user2 = int(input())
user3 = int(input())
user4 = int(input())
def cal(a,b,c,d):
    add_ = a + b + c + d
    sub = a-b-c-d
    mul = a*b*c*d
    div = a/b
    return add_, sub, mul, div
addition = cal(user1,user2,user3,user4)
subtraction = cal(user1,user2,user3,user4)
multi = cal(user1,user2,user3,user4)
divi = cal(user1,user2,user3,user4)
print(addition)
print(subtraction)
print(multi)
print(divi)
output:
10
5
2
1
(18, 2, 100, 2.0)
(18, 2, 100, 2.0)
(18, 2, 100, 2.0)
(18, 2, 100, 2.0)
Usage of %d, %f, %s
print("usage of %%(args))
price = 45.3;grade = 'A';stock = 15
print('%d',%price)
print('%d',%grade)#type error
print('Price is %.f'%price)
print('Price is %.1f'%price)
print('Grade is %s'%grade)

radius_ = 3.5
area_of_circle = 3.1416 * radius_** 2
print('Area of circleis: %.2f'%area_of_circle)

#control block statements ==> they control the flow of the program
#conditional statements (if, elif, else)
#repetition statement loops, (for, while)
#jumping statements (break, continue, pass)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obesity")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
name = input('Enter youe own name : ')
bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obesity")
print(bmi)

weight = float(input("Enter weight in kg: "))
height_cm = float(input("Enter height in cm: "))

height_m = height_cm / 100

bmi = weight / (height_m ** 2)

print("BMI:", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obesity")

weight = float(input("Enter weight in kg: "))
height_cm = float(input("Enter height in cm: "))

height_m = height_cm / 100

bmi = weight / (height_m ** 2)

print("BMI:", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obesity")

weight = float(input("Enter weight in kg: "))
height_feet = float(input("Enter height in feet: "))

height_m = height_feet * 0.3048

bmi = weight / (height_m ** 2)

print("BMI:", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")

elif bmi < 25:
    print("Normal weight")

elif bmi < 30:
    print("Overweight")

else:
    print("Obesity")

name = input("Enter your name: ")

weight = float(input("Enter your weight in kg: "))

unit = input("Enter height unit (feet/cm/inches/meters): ").lower()

height = float(input("Enter your height: "))

if unit == "feet" or unit == 'feets':
    height_m = height * 0.3048

elif unit == "cm" or unit == 'feets':
    height_m = height / 100

elif unit == "inches":
    height_m = height * 0.0254

elif unit == "meters":
    height_m = height

else:
    print("Invalid height unit")

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