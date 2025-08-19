name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))

eligibility = (age < 18) and (score > 70)
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")
'''Candidate: 67
Age: 56
Score: 54
Eligible: False'''

# Federal Government Scholarship Key Eligibility Requirements
Citizen = input("Enter your citizenship")
Citizenship = Citizen == "Nigeria"
print(Citizenship)   # citizenship = Nigeria

# Enrollment
Enrollment = input("Enter enrollment info")
Enrolled = Enrollment == "undergraguate in Nigeria"
print(Enrolled) #undergraguate in Nigeria

# Other_Scholarship
Other_Scholarship =input("are you currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international?")
Scholarship = Other_Scholarship == "No"
print(Scholarship) # No

# Academic Qualification
Qualification = input(" do you have five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.")
Academic_Qualification = Qualification == "Yes"
print(Academic_Qualification)

eligibility = (Citizenship, Enrolled, Scholarship and Academic_Qualification)
print(eligibility)


# Method 2
citizenship = input("Are you a nigerian")
Enrollment = input(" registered, full-time undergraduate student in a recognized Nigerian university?")
Other_Scholarship = input("are you currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international?")
Academic_Qualification = input("do you have five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.")
eligibility = (citizenship == "yes" and Enrollment == "yes" and Other_Scholarship == "no" and Academic_Qualification == "yes")
print(eligibility)

