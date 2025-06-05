def func1():
    name = "Utkarsh"
    return name

def func2():
    name = "Utkarsh"
    name     # it will return None as there is no return type

output1 = func1()
output2 = func2()
print(output1)
print(output2)

# Python is strict in return type