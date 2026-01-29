size=int(input("enter the size : "))
for i in range(size):
    for space in range(size-i-1):
        print(" ", end='')
    for star in range(2*i+1):
            print("*", end= " ")
    print()