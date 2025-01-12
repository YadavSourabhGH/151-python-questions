# Character Frequency in String
user_string = input("Enter a string: ")

char_count = {}

for char in user_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character frequency:", char_count)