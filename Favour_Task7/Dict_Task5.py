# Task5
names = ("Favour", "Joy", "Victor")
phone_numbers = ("08168948275", "08163734431", "08035485146")
combined = dict(zip(names, phone_numbers))
print(combined)
print(combined.get(input("enter a name"), "an error message"))