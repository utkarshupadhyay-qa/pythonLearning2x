# *args and **kargs

# by using *args we are able to pass any number of arguments while calling function

def print_argument(*args):
    for i in args:
        print(i , end= "  ")

print_argument(1)
print_argument(1,2)
print_argument(1,2,3)
print_argument(1,2,3,4)
