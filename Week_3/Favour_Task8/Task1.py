# Task1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"{num1} == {num2} : {num1 == num2}")
# Output: 4 == 5 : false
# It is false because 4 is not equals to 5 comparison, hence the output

print(f"{num1} != {num2} : {num1 != num2}")
# 4 != 5 : True
# It is True because 4 is not equals to 5 comparison, hence the output

print(f"{num1} > {num2} : {num1 > num2}")
# 4 > 5 : False
# It is false because 4 is less than 5

print(f"{num1} < {num2} : {num1 < num2}")
# 4 < 5 : True
# It is True because 4 is greater than 5

# Use cases scenero
# 1. Result spreadsheet to know the number of students that had a particular score or score range in exams
# 2. Login details
# 3. Voting: to streamline the age of people voting

# Login details
email = "favourolaosebikan@gmail.com"
favour_email = email == "favourolaosebikan@gmail.com"
print(favour_email)
