#eg of polymorphism in general
class india:
    def capital(self):
        print("new delhi")

class usa:
    def capital(self):
        print("washington DC")


objind = india()
objusa = usa()

objind.capital()
objusa.capital()
