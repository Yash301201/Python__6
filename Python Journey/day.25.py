'''
print("hello")
# perform operation
a = 15
b = 25
print(a+b)
'''
#Tokens -> Keywords,Variables,Operators,Punctuators
batch = ['pfs-6','da-6']
print(batch)
print(type(batch))
print(len(batch))
#list-> collection->append(),extend(),insert()
batch.append('vishala')
#print(batch)
#print(len(batch))
batch.extend(['swapana','kick'])
print(batch)
#print(len(batch))
batch.insert(0,'ram')
#print(batch)
#print(len(batch))
batch.insert(-1,'python')
#print(batch)
#print(len(batch))
#indexing-- [] ->index starts at 0 and ends at len(obj)-1
#print(batch[0])
#print(batch[4])
#print(batch[34])#indexerror -> length is only 7 we are accessing extra

#Slicing-> group of values [start:end] #start is included ,end is excluded
#print(batch[0:3])
#print(batch[4:6])
#print(batch[3:5])
#last 3 elements-> we prefer negative index value
#print(batch[-3:])
print(batch[:3])
#Striding ->[start:end:step]
print(batch[::3])
print(batch[::-3])#it skip 2 elements from start
print(batch[1:5:2])


#tryout ->such kind
print(batch[:7:4])
print(batch[7::4])
print(batch[1::5])
print(batch[1:7:-2])
print(batch[-1:-4:-1])





