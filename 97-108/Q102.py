# 102.	**Check if a Matrix is Symmetric**

# •	Determine if a given square matrix is symmetric (equal to its transpose).

def is_symmetric(matrix):
    # Check if the matrix is square
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        return False

    # Check symmetry
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Test the function
matrix = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
]

print("The matrix is symmetric:", is_symmetric(matrix))