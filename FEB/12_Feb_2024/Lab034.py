# Continue -> alternate of break

for num in range(1, 10):
    print(num)

print("--------------")

for num in range(1, 10):
    if num > 1:
        print(num)

print("----------------")

for num in range(1, 10):
    if num % 2 == 0:
        print(num)

print("---------------")

for num in range(1, 10):
    if num % 2 == 0:
        print(f"Found even number {num}")
    else:
        print(f"Found odd number {num}")

print("--------------")

# Continue - it will continue the program

for num in range(1, 10):
    if num % 2 == 0:
        print(f"Found even number {num}")
        continue  # if found even number it will take us to 'for' loop
    print(f"Odd number {num}")
