name1 = "Utkarsh"
name2 = 'Utkarsh'
print(name1)
print(name2)
print(type(name1))
print(type(name2))

dir1 = "C:/abc.txt"
print(dir1)
dir2 = 'C:/abc.txt'
print(dir2)

dir3 = 'C:\abc\abc.txt'
print(dir3)

dir4 = "C:\abc\abc.txt"
print(dir4)

dir5 = "C:\\abc\\abc.txt"
print(dir5)

# raw string concept
# this will be helpful in directory path
dir6 = r"C:\abc\abc.txt"
print(dir6)

# Format string
first_name = "Utkarsh"
last_name = "Upadhyay"
age = 28
isMarried = False
print(f"Your name is {first_name} {last_name} , Your age is {age} and you are {isMarried}")