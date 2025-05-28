# Multi-level Inheritance

class GrandFather:

    def home(self):
        print("5 BHK Flat")

class Father(GrandFather):
    def home2(self):
        print("Delhi 2 BHK Flat")


class Son(Father):
    def home3(self):
        print("Noida 3 BHK Flat")

pramod = Son()
pramod.home()
pramod.home2()
pramod.home3()

mmd = Father()
mmd.home()
mmd.home2()
# mmd.home3()   # not accessible

gkd = GrandFather()
gkd.home()
# gkd.home2()   # not accessible as not inherited
# gkd.home3()