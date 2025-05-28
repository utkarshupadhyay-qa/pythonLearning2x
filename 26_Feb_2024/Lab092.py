class Password:

    def __init__(self, password):
        self.__password = password
        self.public_variable = 10

    # F(n) and GET and SET

    def get_password(self, is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("Invalid Password")

    def set_password(self, password):
        if len(password) > 10:
            self.__password = password
            print("Password set to correct")
        else:
            print("Not allowed , weak password")


pwd = Password("Hacker123")
print(pwd.public_variable)
# print(pwd.__password)    -> not accessible
pwd.get_password(True)   # authentication is true
pwd.get_password(False)  # Authentication is false
pwd.set_password("Bro")
pwd.set_password("utkash111111111")