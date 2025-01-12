# Count Special Characters
user_string = input("Enter a string: ")

special_chars = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"

special_char_count = 0
for char in user_string:
    if char in special_chars:
        special_char_count += 1

print("Number of special characters:", special_char_count)