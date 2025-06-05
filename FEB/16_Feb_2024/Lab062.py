# String is a bunch of characters -> also immutable
# Tuples is list of any datatype that cannot be changed
# List is collection of items that can be changed - can make duplicate also
# SET -> collection of unique items -> no duplicate

my_set1 = {1, 2, 3, 2, 4, 5, 4, 5}
print(my_set1)  # duplicate will be eliminated
print(len(my_set1))

# my_set2 = set()
# my_set3 = {}   # both ways we can create empty set

list1 = [33, 32.1, 33, 35.4, 34, 35, 21]
set1 = set(list1)    # set is unordered unique items
print(len(set1))
print(set1)
