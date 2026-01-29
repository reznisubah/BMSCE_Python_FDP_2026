sub1=int(input("enter sub1 marks : "))
sub2=int(input("enter sub2 marks : "))
sub3=int(input("enter sub3 marks : "))
sub4=int(input("enter sub4 marks : "))
sub5=int(input("enter sub5 marks : "))
total=sub1+sub2+sub3+sub4+sub5
print(f"the total out of 500 is {total}")
perc=(total/500)*100
print(f"the total percentage is : {perc} ")

if perc>75:
    print("its A grade")
elif perc>=50:
    print("its B grade")
elif perc>=30:
    print("its C grade")
else:
    print(" fail")