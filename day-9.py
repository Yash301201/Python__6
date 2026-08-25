'''
Dictionaries: 
1. In Python, a dictionary is a collection of key-value pairs.
2. Each key is unique and maps to a specific value.
3. Dictionaries are mutable, meaning you can change their contents after creation.

dict is represented by curly braces {} and key-value pairs are separated by a colon :. 

Dictionaries can be accessed by calling the key, we will get the value from that key.
Syntax: dict_name = {key1: value1, key2: value2, key3: value3}

get(): This method is used to retrieve the value associated with a specific key in the dictionary. 
       If the key does not exist, it returns None (or a specified default value).
Syntax: dict_name.get(key, default_value)
Example:
a = {"name": "Alice", "age": 30}

print(a)
print(a["name"])
print(a.get("name"))
print(a.get("height", "Not specified"))
output: {'name': 'Alice', 'age': 30}
output: Alice
output: Alice
output: Not specified

update(): This method is used to update the dictionary with new key-value pairs or modify existing ones.
Syntax: dict_name.update({key: value})

There is a another way to update the dictionary by using the key and assigning a new value to it.
dict_name[key] = new_value
Example: 
data_ = {"name": "Yash",
        'balance' : 7000,
        'adr' : 4587912,
         'panc' : 'mxp7894'
} 
print(data_)
print(data_['adr'])
print(data_.get('name'))
data_['name'] = "Sai"
print(data_)
print(data_['name'])
data_.update({'name':'Sony','balance' : 8000})
print(data_)
output: 
{'name': 'Yash', 'balance': 7000, 'adr': 4587912, 'panc': 'mxp7894'}
4587912
Yash
{'name': 'Sai', 'balance': 7000, 'adr': 4587912, 'panc': 'mxp7894'}
Sai
{'name': 'Sony', 'balance': 8000, 'adr': 4587912, 'panc': 'mxp7894'}

values(): This method is used to retrieve all the values present in the dictionary.
Syntax: dict_name.values()
Example: 
data_ = {"name": "Yash",
        'balance' : 7000,
        'adr' : 4587912,
         'panc' : 'mxp7894'
}
print(data_.values())
output: dict_values(['Yash', 7000, 4587912, 'mxp7894'])

keys(): This method is used to retrieve all the keys present in the dictionary.
Syntax: dict_name.keys()
Example:
data_ = {"name": "Yash",
        'balance' : 7000,
        'adr' : 4587912,
         'panc' : 'mxp7894'
}
print(data_.keys())
output: dict_keys(['name', 'balance', 'adr', 'panc'])

items(): This method is used to retrieve all the key-value pairs present in the dictionary as tuples.
Syntax: dict_name.items()
Example:
data_ = {"name": "Yash",
        'balance' : 7000,
        'adr' : 4587912,
         'panc' : 'mxp7894',
}
print(data_.items())
output: dict_items([('name', 'Yash'), ('balance', 7000), ('adr', 4587912), ('panc', 'mxp7894')])

clear(): This method is used to remove all the key-value pairs from the dictionary, making it empty.
Syntax: dict_name.clear()
example:
data_ = {"name": "Yash",
        'balance' : 7000,
        'adr' : 4587912,
         'panc' : 'mxp7894',
}
print(data_)
data_.clear()
print(data_)
output: {}  # empty dictionary after clearing all items

pop(): This method is used to remove a specific key-value pair from the dictionary based on the provided key.
Syntax: dict_name.pop(key)
Example:
data_ = {"name": "Yash",
        'balance' : 7000,
        'adr' : 4587912,
         'panc' : 'mxp7894',
}
data_.pop('balance')
print(data_)
output: {'name': 'Yash', 'adr': 4587912, 'panc': 'mxp7894'}

del: This statement is used to delete a specific key-value pair from the dictionary based on the provided key.
Syntax: del dict_name[key]
Example:
data_ = {"name": "Yash",
        'balance' : 7000,
        'adr' : 4587912,
         'panc' : 'mxp7894',
}
del data_['balance']
print(data_)
output: {'name': 'Yash', 'adr': 4587912, 'panc': 'mxp7894'}

Condtional Statements:
1. if statement: This statement is used to execute a block of code if a specified condition is true, if false then another block of code is executed.
Syntax:
if condition:
    # block of code to execute
else:
    # block of code to execute if condition is false
example: 
num = int(input("Enter age of a person: "))
if num >= 18:
    print("Eligible to vote")


2.if-else statement: This statement is used to execute a block of code if a specified condition is true, 
if false then another block of code is executed.
example: 
num = int(input("Enter age of a person: "))
if num >= 18:
    print("Eligible to vote")
else: 
    print("Eligiblity criteria is not to vote")

if-elif-else statement: This statement is used to execute a block of code if a specified condition is true,
if false then another block of code is executed.
example: 
num = int(input("Enter age of a person: "))
if num >= 18:
    print("Eligible to vote")
elif num >= 16:
    print("Eligible to drive")
else:
    print("Not eligible for any activity")    
'''