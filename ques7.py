# Prompt the user to enter a letter
letter = input("Enter a letter: ").lower()  # Convert to lowercase for uniformity

# Check if the letter is a vowel or consonant
if letter in ['a', 'e', 'i', 'o', 'u']:
    print(f"{letter} is a vowel.")
elif letter.isalpha() and len(letter) == 1:
    print(f"{letter} is a consonant.")
else:
    print("Invalid input. Please enter a single alphabetic character.")
