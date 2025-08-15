print("                   TASK 2")
text = "I love PyTHon"
if "python" in text.lower():
    print("The string contains 'python'")
else:
    print("The string does not contain 'python'")    

# Reverse words without using slicing
word = "python"
reversed_text = "".join(reversed(word))
print(reversed_text)

#removing leading and trailing spaces
text = "         Favour           "
print(text.lstrip())
print(text.rstrip())

# vowels in the sentence

word = "Jesus is Lord"
print(word[1]) # E
print(word[3]) # u
print(word[6]) # i
print(word[10]) # o

# converting and multiplying
num = "1234"
set = int(num)
print(set*2)