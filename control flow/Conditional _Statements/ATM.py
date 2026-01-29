min_bal=500
balance=int(input("enter account balance:"))
amount=int(input("enter the amount to withdrawn: "))
if amount > balance-min_bal:
        print("insufficient bal. ")
else :
    balance-=amount
    print(" take ur money")
    print("remaining balance: ", balance)
