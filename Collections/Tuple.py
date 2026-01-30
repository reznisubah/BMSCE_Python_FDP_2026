#def : a tuple is ordered, immutable collection of items.

# Properties: Ordered, immutable(cannot change it or modify it once create), allows duplicates, heterogeneous

myTuple  = (1,2.5, "BMSCE", "A", 4) # one way of creating tuple
print(myTuple)
anotherTuple = tuple(range(10))    # another way of creating tuple
print(anotherTuple)

# Access elements from tuple
print(myTuple[0])
print(myTuple[2])
print(myTuple[1:3])
print(myTuple[-1])
print(myTuple[-2])

# Operations on Tuple.
# 1) Concatenation of 2 tuples using + operator
tuple1 = (1,2,3)
tuple2 = (4,5,6)
resultTuple = tuple1+tuple2
print(resultTuple)

# 2) repetition of tuple
originalTuple = (1,2,3)
repeatedTuple = originalTuple*3
print(repeatedTuple)

# 3) membership of an element inside the tuple
sampleTuple = (1,2,3,4,5,6)
print(3 in sampleTuple)
print(20 in sampleTuple)
print(3 not in sampleTuple)
print(20 not in sampleTuple)

# 4) length of a tuple

Length = len(sampleTuple)
print(Length)

# 5) Index() find out the index of an element in a tuple
index = myTuple.index("BMSCE")
print(index)

# 6)  Count() - counting the number of occurences of an element in1side the tuple
newTuple  = (1,2.5, "BMSCE", "A", 4, 1, "A")
count = newTuple.count(1)
print(count)

# Note - There are only 2 in-built functions in tuple.
# count and index.
# coz tuples are immutable so cant modify.
# thus we have only limited options in tuple