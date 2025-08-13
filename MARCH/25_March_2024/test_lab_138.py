# Firstly we install Faker in terminal by -> pip install faker

from faker import Faker

# Create a Faker instance
fake = Faker()

# Generate a fake name
print(fake.name())
# Output might be something like: "John Doe"

# Generate a fake address
print(fake.address())

# Output might be something like :
# "123 Elm Street
# Apt. 4B
# New York , NY 10014"

