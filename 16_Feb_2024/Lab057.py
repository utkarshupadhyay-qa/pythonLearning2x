# Filter
# It can filter the items from the list based on the logic
# return less number of items

my_list1 = [1, 2, 3, 4, 5, 6]
even_my_list1 = filter(lambda x: x % 2 == 0, my_list1)
print(list(even_my_list1))


# def even(num):
#     return num % 2 == 0
#
# even_numbers = list(filter(even , my_list1))
# print(even_numbers)