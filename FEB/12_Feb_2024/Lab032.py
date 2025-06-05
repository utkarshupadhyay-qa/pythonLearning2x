# Pass -> skip the code

for i in range(10): # range by default start from 0
    print(i)

print("-----------------")

for i in range(10):
    if i == 5:
        pass
    else:
        print(i)

print("-----------------")

for i in range(10):
    if i == 5:
        break
    else:
        print(i)