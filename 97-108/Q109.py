# 109.	**Backtracking: N-Queens**

# •	Implement the N-Queens puzzle using backtracking.

def solve_nqueens(n):
    def is_safe(board, row, col):
        # Check row
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        # Check upper diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check lower diagonal
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        return True
    
    def solve(board, col):
        if col >= n:
            return True
        
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                
                if solve(board, col+1):
                    return True
                
                board[i][col] = 0
        
        return False
    
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    if not solve(board, 0):
        return "No solution"
    
    return board

def print_board(board):
    for row in board:
        print(row)

n = 4
board = solve_nqueens(n)
print_board(board)
