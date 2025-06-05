# Encapsulation  - bind the data variables and methods - but hide the important variables
# Data members / Class Variables and functions - they are closed within a single blueprint
# Wrapping or binding the data variables with the methods

class Car:
    name = None

    def __init__(self,name):
        self.name = name


    def printName(self):
        print(self.name)

xuv = Car("XUV 500")
xuv.printName()

lambo = Car("Lamborghini Aventador")
lambo.printName()

print(xuv.name)
