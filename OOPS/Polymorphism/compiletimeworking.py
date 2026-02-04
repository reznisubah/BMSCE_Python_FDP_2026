def add(a=None,b=None, c= None):
    if a!=None and b!=None and c!=None:
        return a+b+c
    elif a!=None and b!=None:
        return a+b
    else:
        return a

print(add(1,2,3))
print(add(1,2))
print(add(1))

#it is an additional trick to do compile time polymorphism. Officially, compile time polymorphism is not available in polymorphism.