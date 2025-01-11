# 6. Adventure Game - Simple text adventure
def play_adventure():
    print("You're in a dark room with two doors.")
    choice = input("Choose 'left' or 'right' door: ").lower()
    
    if choice == "left":
        print("You found a treasure chest!")
        if input("Open it? (yes/no): ").lower() == "yes":
            return "You found gold! You win!"
        return "You leave the treasure. Game Over!"
    return "You fell into a pit! Game Over!"
print(play_adventure())