# Tuples
# Collection of items
# Tuples are immutable in nature -> items can't be changed
# Tuples can also have multiple datatypes (heterogeneous)

my_tuple1 = (1, 2, 3, 4, 5, 6)
# my_tuple1[0] = 22  # will give type error
print(my_tuple1)
print(type(my_tuple1))
print(len(my_tuple1))

my_list1 = [1, 2, 3, 4, 5, 6, 7]
new_tuple = tuple(my_list1)  # list can be converted to tuple
print(new_tuple)
