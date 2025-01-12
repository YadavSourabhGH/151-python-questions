# 101.	**Transposition of a Matrix**

# •	Compute the transpose of a user-provided matrix.


def transpose_matrix(matrix):
    # Transpose using list comprehension
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transpose

# Test the function
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed = transpose_matrix(matrix)
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed:
    print(row)