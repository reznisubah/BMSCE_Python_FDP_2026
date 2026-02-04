class mom:
    def cook(self):
        print("Indian ")
class daughter(mom):      # apply inheritance here.  # taking it from parent and changing it(called overriding).
                          # how we will take it is thorugh inheritance
    def cook(self):
        print("Chinese ")    # taking it from parent and changing it(called overriding). how we will take it is thorugh inheritance

    def bake(self):
        print("cake")


m = mom()
d = daughter()

m.cook()
d.cook()

