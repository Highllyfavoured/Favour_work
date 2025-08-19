store = {'Book': 10, 'Pen': 20, 'Bag': 5}     
Before_purchase = {'Book': 10, 'Pen': 20, 'Bag': 5}
item = input("Enter item")
quantity = int(input("Enter quantity"))
store[item] -= quantity
print("Before purchase:", Before_purchase)
print("After purchase:", store)


