# Constructor - a special method() which does 2 things.
# 1)   create the object.
# 2)   Initialize objects attributes.
# it is called whenever we have attributes

class student:
    def __init__(self, name, usn):
        self.name = name
        self.usn  = usn

    def printDetails(self):
        print(f"student name is {self.name}")
        print(f"student usn is {self.usn}")

name1 = input("enter a name : ")
usn1 = int(input("enter usn"))

name2 = input("enter a name : ")
usn2 = int(input("enter usn"))

s1 = student(name1, usn1)
s2 = student(name2, usn2)

s1.printDetails()
s2.printDetails()


