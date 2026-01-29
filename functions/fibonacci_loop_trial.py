
n = int(input("enter the number : "))
first = 0
next = 1
print(first, next, end = " ")
sum = 0
for i in range(2, n):
    sum = first + next
    print(sum, end = " ")
    first = next
    next = sum
