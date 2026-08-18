''''
Concantination: Here the adding of two strings, list, tuple is called concantination 
Operators: The operators are used to perform operations to variables and the values 


1. Arithmetic Operators

Used for mathematical calculations.

Operator	Meaning	Example	Result
+	Addition	10 + 3	13
-	Subtraction	10 - 3	7
*	Multiplication	10 * 3	30
/	Division	10 / 3	3.333...
%	Modulus (remainder)	10 % 3	1
//	Floor division	10 // 3	3
**	Exponent	10 ** 3	1000
2. Comparison / Relational Operators

Used to compare two values. The result is always True or False.

Operator	Meaning	Example	Result
==	Equal	10 == 10	True
!=	Not equal	10 != 5	True
>	Greater than	10 > 5	True
<	Less than	10 < 5	False
>=	Greater than or equal	10 >= 10	True
<=	Less than or equal	10 <= 5	False
3. Assignment Operators

Used to assign/update values in variables.

x = 10
x += 5    # x = x + 5 → 15
x -= 5    # x = x - 5 → 10
x *= 2    # x = x * 2 → 20
x /= 2    # x = x / 2 → 10.0
x //= 3   # x = x // 3
x %= 3    # x = x % 3
x **= 2   # x = x ** 2

Common assignment operators:

=, +=, -=, *=, /=, //=, %=, **=

4. Logical Operators

Used to combine conditions.

and

Both conditions must be True.

print(10 > 5 and 20 > 10)
# True
or

At least one condition must be True.

print(10 > 5 or 20 < 10)
# True
not

Reverses the result.

print(not(10 > 5))
# False
5. Bitwise Operators

Work on binary/bits.

Operator	Meaning	Example
&	AND	5 & 3
|	OR	5 | 3
^	XOR	5 ^ 3
~	NOT	~5
<<	Left shift	5 << 1
>>	Right shift	5 >> 1

Example:

5 & 3

Binary:

5 = 101
3 = 011
    ---
    001 = 1

So:

print(5 & 3)
# 1
6. Membership Operators

Used to check whether a value exists in a sequence such as a string, list, tuple, etc.

in
numbers = [10, 20, 30]


print(20 in numbers)
# True
not in
print(50 not in numbers)
# True

Operators: in, not in

7. Identity Operators

Used to check whether two variables refer to the same object in memory.

is
a = [1, 2]
b = a


print(a is b)
# True
is not
c = [1, 2]


print(a is not c)
# True

Operators: is, is not

''''
