def add(a,b):
    result=a+b
    return result
def sub(a,b):
    result=a-b
    return result
def mul(a,b):
    result=a*b
    return result
def div(a,b):
    result=a/b
    return result


while True:
    print("1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit")
    choice = int(input("enter ur choice"))
    num1 = int(input("enter the first number : "))
    num2 = int(input("enter the second number : "))

    #op=input("enter operator")
    match choice:
        case 1:
            result= num1+num2
            print(f"the addition of {num1}+{num2} is : {result}")
        case 2:
            result=num1-num2
            print(f"the subtraction of {num1}+{num2} is : {result}")
        case 3:
            result=num1*num2
            print(f"the multiplication of {num1}+{num2} is : {result}")
        case 4:
            result=num1/num2
            print(f"the division of {num1}+{num2} is : {result}")
        case 5:
            print("ok bye")
            break
        case _:
            print("invalid choice")
