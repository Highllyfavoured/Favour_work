# Task3: Days and Activities Pairing
Days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Friday", "Saturday", "Sunday")
Activity1 = input("monday activities")
Activity2 = input("tuesday activities")
Activity3 = input("wednesday activities")
Activities = (Activity1, Activity2, Activity3)
Days = {"Monday": (Activity1), "Tuesday": (Activity2), "Wednesday": (Activity3)}
print(Days)
combined = zip(Days_of_the_week, Activities)
print(list(combined))
