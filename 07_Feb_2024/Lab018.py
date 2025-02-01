# Assignment Operator

name = "Utkarsh"
# It will store the value of variable literal to the identifier

# Unary operator - it is applied to single literal

age = +95
print(age)
my_bank_bal = -500
print(my_bank_bal)

# Not operator - unary operator ( Works only to booleans) --> also called as Negations
is_married = True
print(not is_married)  # reverse of is_maried

# is operator - Identity operator - checks for identity - returns True or False
a = 5
b = 5
print(a is b) # True

c = 5
d = 6
print(c is d) # False

a = 5
b = False
print(a is b) # False

my_list1 = [1,2,3]
my_list2 = [1,2,3]
print(my_list1 is my_list2) # False --> because identities are in different memory location in case of list

my_str1 = "Utkarsh"
my_str2 = "Utkarsh"
print(my_str1 is my_str2)