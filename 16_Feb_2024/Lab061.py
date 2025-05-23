a = 10
a, b = 10, 20
q, w, e = (10, 20, 30)  # In tuple multiple assignment is possible

# Nested Tuples

hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder woman", "princess")

awesome_team1 = (hero1, hero2)  # tuples contains 2 tuples
print(awesome_team1)  # Here concatenation is not there but nested tuples -> tuples within tuples
print(awesome_team1[0])
print(awesome_team1[1][1])
print(awesome_team1[0][1])

# Search in tuples
cities1 = ("London", "Paris", "Los Angeles", "Tokyo")
print("Paris" in cities1)   # True
print("Moscow" in cities1)   # False
