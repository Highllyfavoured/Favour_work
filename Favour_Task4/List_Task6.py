# Task 6:Word Analyzer
# Ask the user to input a word
word = input("Enter a word: ")
# Print the length of the word
print(len(word))
# Check the case of the word
if word.isupper():
    print("The word is in uppercase.")
elif word.islower():
    print("The word is in lowercase.")
elif word.istitle():
    print("The word is in title case.")
else:
    print("The word is in mixed case or doesn't fit standard case formats.")
# Reverse the word using slicing
print(word[::-1])
