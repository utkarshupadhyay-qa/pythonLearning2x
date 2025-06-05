# Web Automation - Selenium
# Page- You are going to automate


class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def loginconfirm(self):
        if self.password == "Pass123":
            print("You are allowed to enter")
        else:
            print("Invalid user")


amit = VWOLoginPage("amit@amit.com","123")
amit.loginconfirm()

print("-----------------------------")


pramod = VWOLoginPage("pramod@pramod.com","Pass123")
pramod.loginconfirm()  # This loginconfirm() is different than of amit.loginconfirm() function

print(id(amit))   # location where they are stored
print(id(pramod))