t = ("Utkarsh", "Quality Analyst", "Utkarsh")
print(set(t))

set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)  # union of sets  -> they will be merged
print(my_set)

set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
my_set2 = set3.intersection(set4)  # Common element of both sets
print(my_set2)

set5 = {1, 2, 3, 4, 5}
set6 = {4, 5, 6, 7, 8}
my_set3 = set5.difference(set6)  # From set5 remove the duplicates of set6
my_set4 = set6.difference(set5)  # From set6 remove the duplicates of set5
print(my_set3)
print(my_set4)


