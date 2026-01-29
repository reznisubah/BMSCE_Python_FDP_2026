n=int(input("enter the number : "))
fact=1
if n<0:
    print("fact is not possible")
elif n==0:
    print(fact)
else:
    for i in range(1, n+1):
        fact=fact*i
    print(f" factorial is:{fact}")
