print("                    Task 3")
# Output: 'apple', 'banana', 'orange'
text = "apple,banana,orange"
print(text.rsplit(",", 2))

# New line
sentence = "God is good!\nAbsolutely all the time.\nHe is ever faithful!"
print(sentence.splitlines())

# Replacing spaces with underscores
text = "    God can be trusted     "
print(text.replace(" ", "_"))  

# Number of letter a in banana
word = "banana"
count_a = sum(1 for letter in word if letter == "a")
print(count_a)

# check if a string starts with "https://"
url = "https://favour.com"
if url.startswith("https://"):
    print("The string starts with https://")
else:
    print("The string does not start with https://")
    