my_dict = {'a': 1, 'b': 2, 'c': 3}
for k, v in my_dict.items():
    if k == 'b':
        print("b is found ")
    else:
        print("Not found")
    print(k, v)
print('b' in my_dict)

op = 'b' in my_dict
print(op)
