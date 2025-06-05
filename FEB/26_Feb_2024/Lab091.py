class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_variable = 100

    def publicfunction(self):
        print(self.__private_variable)

    def deposit(self, amount):
        self.balance += amount

    def _withdrawl(self, amount):
        self.balance -= amount

    def __showbalance(self):
        print("Your balance", self.balance)

    def if_you_are_authenticated(self, flag):
        if flag:
            self.__showbalance()
        else:
            print("Not Allowed")

    def do_with_by_bank_manager(self, amount):
        self._withdrawl(amount=amount)



jp_chase = BankAccount()
jp_chase.deposit(1000)
# jp_chase._withdrawl(200)   # Not allowed as its protected variable
jp_chase.do_with_by_bank_manager(200)
# jp_chase.__showbalance  # will not be allowed - as its private variable
jp_chase.if_you_are_authenticated(True)
jp_chase.if_you_are_authenticated(False)
jp_chase.publicfunction()
