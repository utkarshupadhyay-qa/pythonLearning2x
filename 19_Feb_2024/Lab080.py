class Multi_param:
    name = None  # Class variable

    def print_information(self, first_name, last_name, age):
        a = 10 # local variable
        print("Your name is:", first_name, last_name, "and your age is: ", age)
        print(self.name)
    # print(a)   # it is not accessible as  'a ' is local variable
obj_ref1 = Multi_param()
obj_ref1.print_information("Amit", "Sharma", 54)
