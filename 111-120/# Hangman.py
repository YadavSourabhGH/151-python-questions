# Hangman
import random
def play_hangman():
    words = ["python", "code", "program", "computer"]
    secret_word = random.choice(words)
    guessed_letters = set()
    tries = 6
    
    while tries > 0:
        display = ''
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter
            else:
                display += '_'
        
        print(f"\nWord: {display}")
        print(f"Tries left: {tries}")
        
        guess = input("Guess a letter: ").lower()
        guessed_letters.add(guess)
        
        if all(letter in guessed_letters for letter in secret_word):
            return "You won!"
        elif guess not in secret_word:
            tries -= 1
    
    return f"Game Over! The word was {secret_word}"
