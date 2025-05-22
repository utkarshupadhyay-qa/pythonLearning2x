# Palindrome


# reverse a string
# str = "Utkarsh"
# rev_str = ""
# for c in str:
#     rev_str = c + rev_str
#
# print(rev_str)

# Reverse a String
def reverse_string(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
    return rev_str


name = reverse_string("Utkarsh")
print(name)


# Palindrome ---> str = rev_str

original_str = input("Enter the String \n")
original_str = original_str.lower()
rev_str = reverse_string(original_str)
print(rev_str)
if original_str == rev_str:
    print("It is a Palindrome String")
else:
    print("It is not a Palindrome String")