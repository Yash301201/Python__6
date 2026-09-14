'''
#list->(index,count)
#Let include tuple in list(Tuples are immutable)
batch=['sai','pfs-06','da-6','saketh','akash','python','anil']
batch.insert(2,('vizag','hyd','vijayawada'))
print(batch)
#print(len(batch))
print(batch[2])
print(batch[2][:2])
print(batch[2][1])
print(batch[2][::2])
print(batch[2].index('hyd'))
#index->frist occurance
#count->returns the count of objects
print(batch[2].count('codegnan'))
#index will rasie error, where as count will return 0
batch.insert(3,['pfs','da','jfs'])
print(batch)
#now let us apply some of list functions in above batch lift
#print(batch[3])
#print(batch[3][1])
#To convert only jfs as upper case ->JFS
batch[3][2]=batch[3][2].upper()
#print(batch[3][2])
#now we wanted to add new course in batch[3] position ->AAA
batch[3].append('AAA')
#print(batch[3])
#print(len(batch))
print(batch)
batch.remove('akash')
print(batch)
#remove->value,pop ->index
batch.pop()#pop by default remove last index value
print(batch)
#batch[2].remove('hyd') #rasie attribute error
#del batch[2][1] #tuple is immutable so we cant insert/remove
# we want to remove entire data but keep the list as it is  ->clear()
batch.clear()
print(batch)
'''
#Lets work on Dictionaries
#dict -> {k:v}, keys must be unique
#keys can be int,float,string,list
details = {}
#print(len(details))
details['batch'] = ['PFS6']
print(details)
details['course'] = ['python']
#print(len(details))
#print(details)
details['students'] = ['sai','hema']
#print(details)
#we want to update the dictionary
details.update({'branch':('hyd','vizag'),
                          'subjects':{'python','aptitude','softskills'}})
print(details)
print(len(details))
#keys(),values(),items()
#first always check the type ->dict ->keys ()
#print(details.keys())# returns only keys
#print(details['batch'])
#details['batch'].extend(['JFS','DA'])
#print(details)
details['students'].extend(['vishala','swapna','kick'])
print(details)
details['subjects'].add('DSA')
print(details)

#Task-> Details -> List,set,Dictionary (use codegnan portal as example)
#exams,mock interviews,project demos

# push too github ->share your link in whatsapp group









