name = 'batman'
print(len(name))   # len starts from 1
print(name[0])
print(name[4])
print(name[5])
print(len(name)-1)
print(name[len(name)-1])

# Strings are immutable - ( that can't be changed )

string = 'Hello'
string = 'HOwdy'
# string[0] = 'M' # TypeError: 'str' object does not support item assignment
print(string)