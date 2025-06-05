# Match case -> its similar to switch case ( in python we dont have switch case )

numbers = int(input("Enter the number beetween 1-6 \n"))
match numbers: # Break is not needed in case of MATCH and CASE
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case 4:
        print("You have entered 4")
    case 5:
        print("You have entered 5")
    case 6:
         print("You have entered 6")
    case _:
        print("No idea of number you have entered")