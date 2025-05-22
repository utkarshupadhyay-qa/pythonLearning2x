# Functions - block of codes which can be executed
# They can return something
# They can't return -> non return function
# They have parameter/arguments
# They don't have parameters

# Define-> Call

def say_hello():# In python always use snake case
    print("Hello") # write the code
# Non retrun type and No parameter/arguments

say_hello()  # calling function


def say_hello_arg(name):
    print("Hello", name)
# Non retrun type and with arguments

say_hello_arg("Utkarsh")  # calling function



def say_hello_args(name,age):
    print("Hello", name , age)
# Non retrun type and with multiple arguments

say_hello_args("Utkarsh" , 24)
say_hello_args(123, True)




def say_hello_arg_default(name="Utkarsh"):
    print("Hello", name)
# Non retrun type and with arguments

say_hello_arg_default()  # calling function
# It will take default value which we have specified in function definition
say_hello_arg_default("Amit") # It will replace default value


def sum_number_argument_ret(a,b):
    return a+b

result = sum_number_argument_ret(5,6)
print(result)

result2 = sum_number_argument_ret("Utkarsh", "Upadhyay") # it will concatenate
print(result2)

result3 = sum_number_argument_ret(a =15,b= 16)
print(result3)

# result4 = sum_number_argument_ret(a= 5,b= "Amit") # will give error as its concatenation is not allowed
# print(result4)