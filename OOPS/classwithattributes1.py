class car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def printDetails(self):
        print(f"car name is {self.name}")
        print(f"car model is {self.model}")
        print(f"car color is {self.color}")


c1 = car("kia", "seltos", "black")
c2 = car("maruthi", "brezza", "white")

c1.printDetails()
c2.printDetails()