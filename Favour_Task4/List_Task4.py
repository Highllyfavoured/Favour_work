# Task 4: Name Organizer
names = input("Enter 5 names separated by spaces: ").split()
names = [name.lower() for name in names]
names.sort()
print("Sorted Names:")
for name in names:
   print(name)