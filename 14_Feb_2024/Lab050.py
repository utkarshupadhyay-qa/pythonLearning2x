# List - collection of items - (duplicate is allowed)

my_list1 = [1,2,3]
my_list2 = [True,1 , 2 , 3, 12.34, "Utkarsh"]

# Indexing  - indexing starts at 0
print("Element at index 0 : ", my_list1[0])

# Changing an element
my_list1[1] = 20
print("List after changing an element in list1 : ", my_list1)

# Append
my_list1.append(4)  # append means add in the end
print("List after appending: ",my_list1)

# Extend
my_list1.extend([5,6])  #add list in a list
print("List after Extending: ",my_list1)

# insert
my_list1.insert(1,'a')
print("List after inserting 'a' at index 1: ", my_list1)

# remove
my_list1.remove('a')
print("List after removing 'a: ", my_list1)

# copy
my_copy_list = my_list1.copy()
print(my_copy_list)

#clear
# my_list1.clear()
print("Initial List: ", my_list1)
print(my_copy_list) # it is still present

print("Index of 3 in the list: ", my_list1.index(3))  # it tells us that where in list (at what index) does the value 3 exists

# sort
my_copy_list.sort()
print(my_copy_list)
my_copy_list.reverse()
print(my_copy_list)

print(my_copy_list[0])
print(my_copy_list[1])
print(my_copy_list[2])
print(my_copy_list[3])
print(my_copy_list[4])

