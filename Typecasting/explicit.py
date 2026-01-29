name= input("enter ur name : ")
birthyear = int(input("enter your birth year: "))
print(type(birthyear))
currentyear = int(input("enter current year: "))
print(type(currentyear))
age = currentyear - birthyear
# print(name + " your age is "+ str(age))     # without formatted string(original printing way)
#print("your name : ", name, "your age: ",age) # without formatted string(original printing way)


# print(f"{name} your age is {age}")    # formatted string type 1
print("{} ur age is {}".format(name,age))    # formatted string type 2
print(type(age))


#without str() or explicit type casting function
# enter your birth year: 1990
# <class 'int'>
# enter current year: 2026
# <class 'int'>
# Traceback (most recent call last):
#   File "D:\BMSCE_FDP_2026\Typecasting\explicit.py", line 6, in <module>
#     print("your age is "+ age)
#           ~~~~~~~~~~~~~~^~~~~
# TypeError: can only concatenate str (not "int") to str

# with str() or explicit type casting function
# enter your birth year: 1990
# <class 'int'>
# enter current year: 2026
# <class 'int'>
# your age is 36
# <class 'int'>