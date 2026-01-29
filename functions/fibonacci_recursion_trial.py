def fib(x):
    if x==0 or x ==1:
        return x
    return fib(x-1) + fib(x-2)

n = int(input("enter the number : "))

for i in  range(n):
    print(fib(i), end = " ")