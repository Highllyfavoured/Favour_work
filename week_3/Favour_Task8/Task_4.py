student = {}
name = input("Input your name")
age = int(input("input age"))
score = [70, 85, 90]
Average_score = 82
student = {
    "name": name,
    "age": age,
    "scores": [70, 85, 90],
    "passed": Average_score >= 50,
    "teenager": (age >= 13) and (age <=19)
    }
Average_score = 82
passed = Average_score >= 50
teenager = (age >= 13) and (age <=19)
teenage = teenager == (age >= 13) and (age <=19)
print("Student Record")
print("name:", name)
print("Age:", age)
print("Scores:", score)
print("Passed:", passed)
print("Teenager:", teenage)


