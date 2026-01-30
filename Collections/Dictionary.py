# def: is mutable, unorderd, collection of key value pairs

# properties: unordered( till pyho 3.7 version. + versions maintain the odrder of insertion)
# mutable
# keys should be unique

# Basic operations
dict1= {'name': 'Rezni', 'age': 35, 'city': 'bangalore'}
print(dict1)
dict2= {'name': 'subah', 'age': 36, 'city': 'kerala'}
print(dict2)
dict3={'name': ['Rezni','subah'], 'ages':[35,40],'cities':['bangalore', 'kerala']}
print(f"the dictionary 3 is :{dict3}")

# Printing dictionaries and accessing the values
print(dict1)
print(dict1['name'])

#adding some values
dict1['job'] = 'teacher'
print(dict1)

#remove the elements
#   1) pop     2) popitem     3) del     4) clear
# pop
dict1.pop('age')
print(dict1)
# popitem - it will delete the latest key from the dict
dict1.popitem()
print(dict1)
# del
print(dict2)
del dict2['age']
print(dict2)

#clear
print(dict3)
dict3.clear()
print(dict3)

# Dictionaries functions : Keys(), values(), items(), get(key), update()
myDict = {'name' : 'rezni', 'age': 35, 'city': 'kochi'}
# 1) Key
key = myDict.keys()
print(key) # directly printng
print(type(key)) # trying to check key type
for i in key:
    print(i) # iterate over keys and printing them separately
print(list(key)) # keys as list

# 2) Values
value = myDict.values()
print(value)
print(type(value))

# 3) Items
item = myDict.items()
print(item)
for i in item:
    print(i) # iterate over keys and printing them separately
print(list(item))

# get()
print(myDict.get('name'))
print(myDict.get('city'))

# update()
myDict.update({'city': 'palakad'})
print(myDict)
