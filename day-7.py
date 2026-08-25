'''indexing 
positive
negative

all_ = [12,[1,'python',[1,2], (78,[6,7])], ['Java', 78]]
print(all_[1][3][1])
output: [6, 7]

data_ = ['python', [1,2,(90,'Details',[67,0]),(78,'student')]]
print(data_[1][2][1][2])
print(len(data_))

output: t 2
Explanation : the function is used to find the number of elements present in the list.

Slicing: 
a = [1,2,3,4,5,6,7,8]
print(a[2:6])
output: [3, 4, 5, 6]

Methods : 
1. append(): This method is used to add an element at the end of the list.
syntax : list_name.append(value)
example: go = [1,2,3,4]
         print(go.append(5)) 
output : [1, 2, 3, 4, 5]  
2. insert(): This method is used to add an element at the specified index position.
syntax : list_name.insert(index_position, value)
example: go = [1,2,3,4]
         print(go.insert(2, 5))
output : [1, 2, 5, 3, 4]
3. extend(): This method is used to add multiple elements at the end of the list.  (Only iterable objects can be added using extend() method)
syntax : list_name.extend([value1, value2, value3])
example: go = [1,2,3,4]
            print(go.extend([5,6,7]))
output : [1, 2, 3, 4, 5, 6, 7]
4. remove(): This method is used to remove the specified element from the list.
syntax : list_name.remove(value)
example: go = [1,2,3,4]
         print(go.remove(3))
output : [1, 2, 4]
5. pop(): This method is used to remove the element at the specified index position.
syntax : list_name.pop(index_position)
example: go = [1,2,3,4]
         print(go.pop(2))
output : [1, 2, 4]
 
Tuple: It is the collection of the different datatypes that separated by " , " and represented by ()
1.It is inmutable.
2.We can pass a tuple values and that can be assign to the different variables. But should be same number of variables and values.

Example : name, age, gender = ('John', 25, 'Male')
          print(name)
          print(age)
          print(gender)

Max(): This function is used to find the maximum value from the given tuple.
so = (1,2,3,4,5)
print(max(so)) 
output : 5

Min(): This function is used to find the minimum value from the given tuple.
so = (1,2,3,4,5)
print(min(so))
ouput : 1

Count(): This function is used to find the number of occurrences of the specified element in the tuple.
so = (1,2,3,4,5,1,2,3)
print(so.count(1))
output : 2



'''