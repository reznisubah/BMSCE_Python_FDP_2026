n1=int(input("enter the first num : "))
n2=int(input("enter the second num : "))
n3=int(input("enter the third num : "))

if n1>n2 and n1>n3:
    print(f"{n1}  is the largest")
elif n2>n1 and n2>n3:
    print(f"{n2} is the largest")
else:
    print(f"{n3} is largest")