class MyClass:
    def __init__(self):
        self.name = "Amit"

    def public_func(self):
        print("Public Func()")

    def __private_func(self):
        print("This is private")

    def public_fun_privateaccess(self):
        self.__private_func()    # This function can call private function - as its inside the class

a = MyClass()
a.public_func()
# a.__private_func()   # not allowed - as its private function , so not allowed outside class
a.public_fun_privateaccess()

# Security - not everyone can access your variables and functions