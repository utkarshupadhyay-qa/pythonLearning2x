def make_pizza(*toppings):
    print(toppings)
    for n in toppings:
        print(n)


a1 = make_pizza("Mushroom")
a2 = make_pizza("mushroom", "paneer", "pineapple")
a3 = make_pizza("onion", "tomato")
a4 = make_pizza("tomato", "jalapeno", "paneer")
a5 = make_pizza("paneer", "chilly", "mushroom", "onion", "tomato")

print("--------------------------------------------------")


def make_pizza_base(*toppings, base):
    print(toppings, base)
    for n in toppings:
        print(n)
    return toppings, base

p1 = make_pizza_base("mushroom", "paneer", "pineapple", base="thin")
p2 = make_pizza_base("tomato", "jalapeno", "paneer", base="thick")
p3 = make_pizza_base("paneer", "chilly", "mushroom", "onion", "tomato", base="smoky")

print(p1)
print(p2)
print(p3)


print("-------------------------------------------")

p1_topping, p1_base = make_pizza_base("mushroom", "paneer", "pineapple", base="thin")
print(p1_topping)
print(p1_base)

# def make_pizza_base(*toppings, * base): ->>   multiple star parameters is not allowed
