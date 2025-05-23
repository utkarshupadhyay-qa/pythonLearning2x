# Map() -> it is a function
# Python is a built-in function.
# Applies a given function to each item of an iterable (such as a list, tuple, or string) and returns an iterator with the results.
# map() function is often used when you need to transform each element of an iterable using a specific function and collect the results

def sq_of_number(num):
    return num ** 2


# result = sq_of_number(10)
# print(result)

number = [1, 2, 3, 4, 5]

# Map() ->
# 1- it takes each item from the list
# 2 - execute the function on it .
# 3- returns same number of elements (list)

sq_numbers = list(map(sq_of_number, number)) # convert it into list so that it does'nt return map
print(sq_numbers)