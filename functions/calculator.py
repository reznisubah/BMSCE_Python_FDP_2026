def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

while True:
    op = int(input("enter operator \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit \n"))
    if op<5:
       num1 = int(input("enter the first number : "))
       num2 = int(input("enter the second number : "))
    else:
        break

    match op:
        case 1:
            print(f"the addition of {num1}+{num2} is : {add(num1,num2)}")

        case 2:
            print(f"the subtraction of {num1}-{num2} is : {sub(num1,num2)}")
        case 3:
            print(f"the mul of {num1}*{num2} is : {mul(num1,num2)}")
        case 4:
            print(f"the div of {num1}/{num2} is : {div(num1,num2)}")
        case 5:
            print("ok bye")
            break
        case _:
            print("invalid choice")
