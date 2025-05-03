# Problem statement - Find the maximum of three numbers
num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))
num3 = int(input("Enter number 3"))

# max_num = max(num1,num2,num3)
# print((max_num))
# what if max function is not availiable

if num1 > num2 and num1 > num3:
    print("Max number is ", num1)
elif num2 > num1 and num2 > num3:
    print("Max number is ", num2)
else:
    print("Max  number is ", num3)

