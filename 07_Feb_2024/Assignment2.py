# Task 1
# Write a Python program to calculate the area of a circle given its radius
# using the formula area=π×r^2 ( Take pie as 3.14)

# Task 2
# Create a program that takes two numbers as input and prints
# whether the first number is greater than, less than, or equal to the second number.

# Task 3
# Develop a Python script that calculates the square and cube of a given number.

# Task 1

radius1 = float(input("Enter the radius of the circle: "))
pi = 3.14
area1 = pi*radius1**2
print("The are of the circle is: ",area1)

# Task2

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
print("Is first number greater than second number :{} ".format(first_number > second_number))
print("Is first number less than second number : ",first_number < second_number)
print("Is first number equal to second number :{} ".format(first_number == second_number))

#Task 3

number1 = int(input("Enter the given number for whom we want to calculate the square and cube: "))
print("The square of the number {} is {} ".format(number1,number1**2))
print("The cube of the number {} is {} ".format(number1,number1**3))
