'''

Iteration in Python

for statement: The for statement in Python is used to iterate over a sequence (like a list, tuple, string) or other iterable objects. It allows you to execute a block of code repeatedly for each item in the sequence.
Syntax: for variable in sequence:
Example:
num = [1, 2, 3, 4, 5]
for n in num:
    print(n)
output: 
1
2   
3
4
5
Example2: 
nums = 'python'
for num in nums:
    print(num)
output:
p
y
t
h
o
n

else in for loop: unlike if-else, else block in for statment is executed after completed of all iterations 
example: 
num  = 'python'
for num in nums:
    print(num)
else:
    print('for ended')

output: 
p
y
t
h
o
n
for ended

example3 : 

Control statements: 
. break → exit the loop completely

It stops the loop.

for i in range(1, 6):
    if i == 3:
        break
    print(i)

Output:

1
2

When i == 3, break says:

Stop the loop now.

2. continue → skip current iteration

It doesn't stop the loop. It skips the current iteration and goes to the next one.

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

Output:

1
2
4
5

When i == 3:

Skip 3 and continue with the next iteration.

3. pass → do nothing

pass doesn't stop or skip anything. It simply means:

Do nothing here.

for i in range(1, 4):
    if i == 2:
        pass
    print(i)

Output:

1
2
3

The loop continues normally.

assert: it is a keyword used to check the condition, increase the condition is false, it will raise the error (assertionerror)

age = 25
assert age >= 19, 'not eligible to vote'
print('your eligibe to vote')
output: your eligible to vote

While loop: 

num = 1 
while(num <= 5):
    print(num)
    num += 1
print(num)
output: 
1
2
3
4
5
6

'''