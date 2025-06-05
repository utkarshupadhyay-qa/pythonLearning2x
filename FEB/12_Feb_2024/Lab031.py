# Break
# For -> 1 to 10 -> range(1,11,1) , range(1,11)
#i =5 -> break out from loop -> kicked out from the loop

for counter in range(1,11):
    if counter == 5:
        break
    print(counter)
print("Outside of the FOR loop")


for counter in range(1,11):
    print(counter)
    if counter == 5:
        break
print("Outside of the FOR loop")