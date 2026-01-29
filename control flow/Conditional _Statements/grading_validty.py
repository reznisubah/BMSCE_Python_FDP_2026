sub1=int(input("enter sub1 marks : "))
sub2=int(input("enter sub2 marks : "))
sub3=int(input("enter sub3 marks : "))
sub4=int(input("enter sub4 marks : "))
sub5=int(input("enter sub5 marks : "))
total=(sub1+sub2+sub3+sub4+sub5)
if sub1>0 and sub1<=100:
    if sub2>0 and sub2<=100:
        if sub3>0 and sub3<=100:
            if sub4>0 and sub4<=100:
                if sub5>0 and sub5<=100:
                    print(f"the total out of 500 is {total}")
                    perc = (total / 500) * 100
                    print(f"the total percentage is : {perc} ")

                    if perc > 75:
                        print("its A grade")
                    elif perc >= 50:
                        print("its B grade")
                    elif perc >= 30:
                        print("its C grade")
                    else:
                        print(" fail")
                else:
                    print(" sub5 marks are invalid")
            else:
                print("sub4 marks are invalid")
        else:
            print("sub3 marks are invalid")
    else:
        print("sub2 marks are invalid")
else:
    print("sub1 marks are invalid")
