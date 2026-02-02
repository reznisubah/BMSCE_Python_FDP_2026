class Animal:
    def eat(self):
        print("eating....")

class dog(Animal):
    def bark(self):
        print("BARKING....")
class cat(Animal):
    def meow(self):
        print("meowwwwww.......")

a = Animal()
d = dog()
c = cat()

a.eat()   # object of animal class ( parent class)
d.eat()     # parent class
d.bark()    # own function
c.meow()  # object of cat class(its own function)
c.eat()  # parent class
