# # Task 4: Create a Unique Voters Registration System
# Initialize an empty set to store unique voter names
voters = set()

# Ask how many voters to register
num = int(input("How many voters will register? "))

# Loop to collect voter names
for i in range(num):
    name = input(f"Enter name of voter {i+1}: ").strip().lower()
    
    if name in voters:
        print("⚠️ Warning: This voter is already registered.")
    else:
        voters.add(name)
        print("✅ Voter registered successfully.")

# Display total number of unique voters
print(f"\nTotal unique voters registered: {len(voters)}")