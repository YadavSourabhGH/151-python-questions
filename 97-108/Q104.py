# 104.	**Longest Common Subsequence (LCS)**

# •	Implement the LCS algorithm for two sequences.

def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

s1 = "abcde"
s2 = "ace"
print(lcs(s1, s2))  # Output: 3
# The longest common subsequence is "ace"
