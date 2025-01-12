# 107.	**Knapsack Problem (0/1 DP)**

# •	Implement the 0/1 Knapsack using dynamic programming.

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
    
    return dp[n][capacity]

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print(knapsack(values, weights, capacity))  # Output: 220
