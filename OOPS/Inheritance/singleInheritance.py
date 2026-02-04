class Animal:
    def eat(self):
        print("eating....")

class dog(Animal):
    def bark(self):
        print("BARKING....")

a = Animal()
d = dog()

a.eat()

d.eat()
d.bark()