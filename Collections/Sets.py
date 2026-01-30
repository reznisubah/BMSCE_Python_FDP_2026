# def: a set is an unorered collection of unique elements

# properties :  unoredered(order of hashing is considered), mutable, does not allow duplicates

mySet = {1,2,3,4}
print(mySet)

# Adding elemets
mySet.add(5)
print(mySet)
mySet.add(3)
print(mySet)
# Remove elemets
mySet.remove(2)
print(mySet)
mySet.discard(2)
print(mySet)
# discrad and remove does the same thing. but we are trying to remove after removing, it ell giv error. but discard will not
mySet.pop()
print(mySet)  # since it is unordered, it will delete element arbitrarily.
# unlike list, it will follow the order. or not delete the last element

setA={1,2,3}
setB={3,4,5}
union = setA | setB  #{1,2,3,4,5}
print(f" union is : {union}")
intersection = setA & setB
print(f"interscetion is : {intersection}")
difference = setA-setB
print(f"deifference is: {difference}")

