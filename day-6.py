'''
Indexing : 
Indexing is used to get character that you looking to access

We have two types: 
1.Positive indexing : The starting point or postion will be 0 in the array 
print(variable_name[index_position])
text = "python"
print(text[2])
2.Negative indexing : The starting point or position will be -1 in the array 
text = "python"
print(text[-2])
Example : 
txt = "Python is a programming language"
print(txt[17])
print(txt[-15])

Methods:
len(): Which is in-built function is used to get number of characters present in string. 
Syntax : print(len(variable_name))
-------------------------------------------------------------------------------------------------
Slicing: This is used to access the particular part from the string  
Syntax : print(varibale_name[start:end:step])
print(txt[12:23:1])
output: programming
print(txt[:])
output: Python is a programming language
print(txt[12:])
output: programming language
print(txt[:23])
output: Python is a programming
print(txt[:33])
output: Python is a programming language
print(txt[-1:-33:-1])
output : egaugnal gnimmargorp a si nohtyP
print(txt[::])
output : Python is a programming language
---------------------------------------------------------------------------------------------------
Upper() : Used to convert lower cases alphabets to capital alphabets 
synatx : print(varible_name.upper())
print(txt.upper())
output: PYTHON IS A PROGRAMMING LANGUAGE 

Lower(): used to convert all captials into lower case.
syntax : print(variable_name.lower())
print(txt.lower())

index(): We pass the character in the index syntax then we get output as index position but not character.
Syntax : print(variable.index(value, start,end))
         print(varibale.index(substring, start,end))    
example : 
txt = "Python is a programming language"
print(txt.index("i", 13, 24))
output : 20

replace() : Used to replace old substring with new substring 
syntax: print(varible.name.replace('old', 'new'))  
print(txt.replace('Python', 'orange'))
output: orange is a programming language   

split() : this method is used to separate string based on the given substring 
syntax: 
print(txt.split(' '))
output: ['Python', 'is', 'a', 'programming', 'language']
"all_ =  (txt.split(' '))
print(len(all_))" this is one method 
another method : 
"all_ =  (txt.split( ))
print(all_)"
output : 5 

count() : Used to count number of occrance of substring
syntax: print(variable_name.count(substring, start, end))
print(txt.count('s'))
output: 1
'''