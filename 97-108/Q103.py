# 103.	**Longest Common Substring**

# •	Find the longest common substring between two given strings.

def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    max_len = 0
    end_index = 0
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0
    
    return s1[end_index-max_len:end_index]

s1 = "abcde"
s2 = "abfce"
print(lcs(s1, s2))  # Output: ab
# The longest common substring is "ab"