# Class and Objects
# Class - Attributes and Behaviour
#  class is a blueprint or template that defines the attributes (variables) and behaviors (methods) that objects of that class will have.
# Person class -> Object- Amit , Ajay , Lakshya

class Person:
    name = None    # Person class -> Attributes ---> Data members
    age = None
    id = None
    phone_num = None
    # Behaviour ---> methods (not functions)
    def talk(self):  # self--> means own instance --> always first argument of all methods within the class
        print("I can talk")

    def sleep(self):
        print("I am a method")   # Methods are part of classes
        print("I can sleep")

    def walk(self):
        return "I am walking"

def another_function():
    print("I am a function")   # This is independent function -> not part of class


# Objects  --> ClassName()
amit = Person()
amit.name = "Amit"
print(amit.name)
amit.talk()  # This belongs to Amit object

ajay = Person()
lakshya = Person()

# Nothing is there -> so clean the memory after execution of program
# Exit the program
