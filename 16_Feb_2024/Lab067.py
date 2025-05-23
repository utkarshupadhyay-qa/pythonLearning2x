# Dictionary -> key value pair

name = "Utkarsh"  # this is not dictionary
# key->"name"
# value->"Utkarsh"

# A Dictionary is unordered collection of data in key-value pair format
# If we don't use dict() keyword then we have to use keys in " "

my_dict = {}  # Assignment is done using :
my_dict1 = dict()  # Assignment is done using =
print(type(my_dict))
print(type(my_dict1))

phone_book = {"Utkarsh": 123456, "Amit": 345678, "Akash": 6789045}
print(len(phone_book))
print(phone_book["Utkarsh"])  # Here keys will be given to access data - not index
print(phone_book["Akash"])

phone_book2 = dict(Batman=1234, Superman=4567, Ironman=567890)
print(phone_book2)
# print(phone_book2[Ironman])  # will give error
print(phone_book2["Ironman"])
print(phone_book2["Ironman"])
print(phone_book2.get('Ironman'))
print(phone_book2.get("Ironman"))

utkarsh_details = dict(name="Utkarsh", age=29, isMale=True, Address="UP")
utkarsh_details2 = {"name": "Utkarsh", "90": 29.29, "isMale": True, "Address": "UP"}
print(utkarsh_details2.get(90))  # None will be output because key is in string
print(utkarsh_details2.get("90"))
# print(utkarsh_details2[90])   # will give key error
print(utkarsh_details2["90"])
print(utkarsh_details2['90'])

my_dict2 = {"a": 1, "b": 2, "c": 3, "a": 95}
print(len(my_dict2))  # length will be 3 not 4 because last key value cannot be duplicated and last value will be taken.
# Keys will be unique ,values can be duplicate

print(my_dict2)
