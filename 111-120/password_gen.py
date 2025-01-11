# 1. Password Generator - Creates a random password of specified length
import random

def generate_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    for i in range(length):
        random_index = random.randint(0, len(characters) - 1)
        password += characters[random_index]
    return password

print(generate_password())
