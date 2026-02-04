from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    def run(self):
        print(" running ...")

class dog(Animal):
    def eat(self):
        print("dog food")
    def bark(self):
        print("barking..")

#a = Animal()   this will give u an error. coz animal class is hidden
d = dog()


d.eat()     # parent class
d.bark()    # own function
