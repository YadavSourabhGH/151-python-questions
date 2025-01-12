# 110.	**Shortest Path in a Grid**

# •	Given a 2D grid, find the shortest path from top-left to bottom-right, moving only down or right (use BFS or DFS).


def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = [(0, 0, 0)]
    
    while queue:
        row, col, steps = queue.pop(0)
        
        if row == rows-1 and col == cols-1:
            return steps
        
        visited[row][col] = True
        
        # Move down
        if row+1 < rows and not visited[row+1][col]:
            queue.append((row+1, col, steps+1))
        
        # Move right
        if col+1 < cols and not visited[row][col+1]:
            queue.append((row, col+1, steps+1))
    
    return -1

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(shortest_path(grid))  # Output: 6
# The shortest path is 1 -> 2 -> 3 -> 6 -> 9
# Total steps = 4