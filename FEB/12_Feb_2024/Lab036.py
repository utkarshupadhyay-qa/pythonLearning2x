# Factorial

number = int(input("Enter the factorial number: \n "))
if number < 0:
    print("Factorial not possible")
elif number == 0:
    print("Factorial of 0 is : \n", 1)
else:
    fact = 1
    for i  in range(1, number + 1):  # here (number +1) because for loop will go till (number-1) only
        fact = fact *i
    print(f"Factorial of {number} is {fact}")