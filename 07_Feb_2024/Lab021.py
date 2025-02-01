# String Concat

str1 = "Hello"
str2 = "World"
str3 = str1 + str2
print(str3)

name1 = "Utkarsh"
age1 = 29
# r = name1 + age1    # TypeError: can only concatenate str (not "int") to str
r = name1 + str(age1)
print(r)

g = "Hello"
g += "World"  # g=g+"World"
print(g)

# Increment Decrement Operator -> ++ ,--

x = 5
x-= 1
print(x)

y = 5
y -= 1
print(y)

y = 10
# z = ++y
# Increment Decrement operator not allowed in python

