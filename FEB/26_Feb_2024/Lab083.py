class Person:
    # Class variables/Instance variables
    name = "Amit"   # we cannot keep anything empty , means we have to assign something
    age = None

    def walk(self):
        a = 10   # Local Variables
        print("Hi Your name is ", self.name)
        print("Hi Your age is: ", self.age)
        print(a)

amit = Person()
amit.walk()   # It will take hardcoded value of name = "Amit"

pramod = Person()
pramod.walk()   # It will take hardcoded value of name = "Amit"  -> to change it we use 'Constructors'