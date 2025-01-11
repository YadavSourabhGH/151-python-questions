# 7. Rock Paper Scissors - Classic game
def play_rps():
    import random
    
    # Game rules: key beats value
    rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    # Get choices
    player = input("Choose rock, paper, or scissors: ").lower()
    computer = random.choice(list(rules.keys()))
    print(f"Computer chose: {computer}")
    
    # Determine winner
    if player == computer:
        return "Tie!"
    elif rules[player] == computer:
        return "You win!"
    return "Computer wins!"