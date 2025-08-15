# Task2: Shopping List Manager
shopping_items = []
for a in range(3):
    item = input(f"Enter shopping list {a+1}: ")
    shopping_items.append(item)
    print("shopping Items:",",".join(shopping_items))
