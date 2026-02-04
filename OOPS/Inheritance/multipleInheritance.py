class mom:
    def cook(self):
        print("cooking....")

class dad:
    def sleep(self):
        print("sleeping....")

class child(mom, dad):
    def study(self):
        print("studying..")

m = mom()
d = dad()
c = child()

m.cook()
d.sleep()
c.study()
c.sleep()
c.cook()

