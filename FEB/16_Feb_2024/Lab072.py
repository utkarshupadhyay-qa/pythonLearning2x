api_response = {
    "first_name": "Utkarsh",
    "age": 29,
    "last_name": "Upadhyay",
    "email": "abc@gmail.com",
    "password": "abc@1234",
    "commission": 10
}
print(api_response)
print(type(api_response))
print(api_response.get('password'))
print(api_response['password'])


api_response['password'] = 'ttt@12345'   # Dictionary is mutable in nature
print(api_response)

for key, value in api_response.items():
    print(key, " --> ", value)

