#definition - a list is  ordered, mutable collection of items.

#Properties are: Ordered, mutable, Allow duplicates

myList = [1,2,3,4,5]  # syntax using []
print(f"the my list is : {myList}")
#anotherList = list(range(100))    # this will create a list from 1 to 100.
anotherList = list(range(2, 101, 2))

#operation on list
# 1) Access elements from mylist
print(f" the 3rd index we have {myList[3]}")
print(myList[2:4])     # [3,4] is the output . and this is called slicing operation.
                       # take a slice from the list. most used operation in data analysis

print(anotherList[10:25]) # from 10th index it will go upto 24th index
print(f" the 24th index we have {anotherList[24]}")
print(f"On the last index we have {anotherList[-1]}") # in this example -ve index starts from the last element in the list

# 2) Modifying the elements. Since list are mutable, we can modify.

myList[3] = 400
print(f"the updated my list is : {myList}")

# 3) Printing the list. List or any collection can be printing in 2 ways.
print(f" the one way of printing is : {myList}")   # 1st way
for i in myList:    # 2nd way
    print(i, end = " ")
print()

# 4) Adding an elements to a list
# append(). it will add the element at the last of the list

myList.append(6)
myList.append(7)
print(myList)
for i in range(8,11):
    myList.append(i)
print(myList)

# insert (). it will insert the element at a particular position in the list
myList.insert(6, 5000) # at index 6, it will insrt 5000
print(myList)
myList.insert(3, "BMSCE")
print(myList)

# 5) Removing elements from the list
myList.remove(5000)
print(myList)
myList.pop()   # remove the last element automatically
print(myList)
del myList[3]
print(myList)

# 6) other functions
print(f" length of my list is: {len(myList)}")
myList.sort()
print(myList)
myList.sort(reverse=True)
print(myList)