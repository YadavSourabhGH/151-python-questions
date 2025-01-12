# 99.	**Matrix Addition**

# •	Prompt the user for two matrices (2D lists) of the same dimensions and compute their sum.

def input_matrix(rows, cols):
    print(f"Enter the elements of a {rows}x{cols} matrix row by row:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        while len(row) != cols:
            print(f"Row {i + 1} must have {cols} elements. Try again.")
            row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)
    return matrix

def add_matrices(A, B):
    # Dimensions of matrices
    m = len(A)
    n = len(A[0])
    
    # Resultant matrix of size m x n
    result = [[0] * n for _ in range(m)]
    
    # Add matrices
    for i in range(m):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
    return result

# Input dimensions for matrix A
rows_A = int(input("Enter the number of rows in Matrix A: "))
cols_A = int(input("Enter the number of columns in Matrix A: "))

# Input dimensions for matrix B
rows_B = int(input("Enter the number of rows in Matrix B: "))
cols_B = int(input("Enter the number of columns in Matrix B: "))
if rows_A != rows_B or cols_A != cols_B:
    print("Matrix addition not possible. Matrices must have the same dimensions.")

else:
    # Input matrices
    A = input_matrix(rows_A, cols_A)
    B = input_matrix(rows_B, cols_B)
    
    # Add matrices
    result = add_matrices(A, B)
    
    # Display result
    print("\nResultant Matrix:")
    for row in result:
        print(row)

        