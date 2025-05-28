# Single Inheritance

class Father:
    gold = "5 Kilograms"
    __private_villa = "GOA"

    def drive_car(self):
        print("Lamborghini")

    def threeBHKflat(self):
        print("3 BHK Flat")

    def private_villa_access(self,is_my_son):
        print(self.__private_villa)

class Son(Father):  # Son is inheriting class
    pass


pramod = Son()
pramod.drive_car()  # Son class does'nt have any code but still it inherits property of father class
pramod.threeBHKflat()
print(pramod.gold)
# print(pramod.__private_villa)  # not allowed because of private variable
pramod.private_villa_access(True)



mmd = Father()
mmd.drive_car()
mmd.threeBHKflat()
print(mmd.gold)
