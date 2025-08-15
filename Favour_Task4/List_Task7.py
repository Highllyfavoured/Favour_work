# TASK 7

# Step 1: Create a list of five cities
cities = ["Lagos", "Cairo", "Nairobi", "Accra", "Dakar"]

# Step 2: Replace the third city (index 2) with a new one entered by the user
new_city = input("Enter a new city to replace the third one: ")
cities[2] = new_city

# Step 3: Remove the last city
cities.pop()

# Step 4: Add a new city to the beginning of the list
first_city = input("Enter a city to add to the beginning of the list: ")
cities.insert(0, first_city)

# Step 5: Print the updated list
print("Updated list of cities:", cities)