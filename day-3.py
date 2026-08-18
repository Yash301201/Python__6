'''Datatypes and type conversions 
-------------------------------

1.Numeric Datatypes 
--------------------
-->Float and int are called as Numerical Datatypes.
Float:
A number which contains decimal values are called as Float datatypes.
eg:56.89
Integer(Int):

2.String
---------
--> String is a sequence of char taht are enclosed in ' '," ",""" """....
String is immutable
eg:
any_ = 'python is a computer Language'
all_ = 'Ab,&[)-+'

3.List
--------
--> List is a collection of different datatypes and it is represented by [] that are sperated by , ...
-->inside the list we call it as items
-->List is Mutable
eg:
any_ = [1,2,3,4(5,6)]
for item in any_:
    print (item)

4.Tuple
--------
-->Tuple is collection of different datatypes taht are enclosed in () and those are seperated by ,.
-->it is immutable.
eg:
nums=(09,24.25,'python',[3,4],(8,9))
5.Dictionary
------------
-->A dictionary stores data as key-value pairs.keys and vaalues are seperated by : ...
key and value pairs are also called as items and this items are seperated by , ...
Dict is represented using {}...
In keys place we can use immutable datatypes.
In value place we can use any data.
eg:
data_ = {1,2,
         name:'Teja',
         (2,3):'tuple'}
    print(data_)

6.Set
------
--> A set stores a collection of unique values.
Set does not allow any duplicate values.
Set is represented by {} and the elements are sperated by ,...
eg:
an={1,2,3.4}
print(an)

TYPE CONVERTIONS:
-----------------
float----> int,str
eg:
int()
price=45.67
print(int(price))

str()
price=45.44
con = str(price)
print(type(con))

integer---->float,str
eg:
float()
num=78
printa(float(num))

str()

num=78
con=str(num)
print(type(con))

String ----> int,float

eg:
int

do='10'
print(int(do))

float
do='10.9'
print(float(do))

list----> Tuple, string
eg:
nums=[1,2,3,4]
print(tuple(nums))

Tuple ----> List()
eg
all_=(5,6,7)
print(tuple(all_))

Set----> tuple,list

eg:
tuple()
all={5,6,7}
print(tuple(all_))

Dict ----> List
eg:
list()
Details=[('name','teja',('edu','b.tech')]
"""	
