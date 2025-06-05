# Handle Exception
# try and except block
# try -> try the code
# except - execute except code (if problem in try)

a = int(input("Enter num 1\n"))
b = int(input("Enter num 2\n"))
100
try:
    c = a / b  # ZeroDivisionError: division by zero
    print("Div is ", c)
except Exception as e:
    print(e)
    print("Zero Division, Please dont use B as zero!")

print("This is Important message that we need show to user!")