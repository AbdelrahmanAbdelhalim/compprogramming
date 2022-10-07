# Backward DP bottom up (No other solution provided on algo monster

def unique_paths(m: int, n: int) -> int:
    dp = [[0 for i in range(m)] for j in range(n)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if i - 1 >= 0:
                dp[i][j] += dp[i - 1][j]
            if j - 1 >= 0:
                dp[i][j] += dp[i][j-1]
    return dp[-1][-1]

