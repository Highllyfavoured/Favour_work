# Task4: Unique Members Registration
names = input("enter three names separated by a comma")
name_lengths = {name: len(name) for name in names}
print("\n\t--- Name Length Dictionary ---")
for name, length in name_lengths.items():
    print(f"\t{name}:\t{length} characters")
