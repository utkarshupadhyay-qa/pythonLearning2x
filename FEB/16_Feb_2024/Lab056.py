# Map() -> is always used on set of items like set , list , tuples , dictionary

import math
def sq_rt(num):
    return math.sqrt(num)


my_list = [21, 34, 54]
sq_rt_list = list(map(sq_rt , my_list))
print(sq_rt_list)

