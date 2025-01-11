#tick tack toe
def play_tictactoe():
    # Create an empty board
    board = [" " for _ in range(9)]
    
    def show_board():
        # Display the 3x3 grid
        for row in range(0, 9, 3):
            print(f"{board[row]} | {board[row+1]} | {board[row+2]}")
    
    for turn in range(9):
        show_board()
        player = "X" if turn % 2 == 0 else "O"
        position = int(input(f"\nPlayer {player}, choose position (1-9): ")) - 1
        
        if board[position] == " ":
            board[position] = player
        else:
            print("Position already taken!")
            continue
            
        # Check for win
        winning_combinations = [
            [0,1,2], [3,4,5], [6,7,8],  # rows
            [0,3,6], [1,4,7], [2,5,8],  # columns
            [0,4,8], [2,4,6]  # diagonals
        ]
        
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
                show_board()
                return f"Player {player} wins!"
    
    return "It's a tie!"

print(play_tictactoe())