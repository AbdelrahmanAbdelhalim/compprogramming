# Bottom up Solution (all me)
def minimum_total(triangle: List[List[int]]) -> int:
    dp = [[math.inf for i in range(len(triangle) + 1)] for i in range(len(triangle[-1]) + 1)]
    dp[0][0] = 0
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + triangle[i][j])
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + triangle[i][j])
    return min(dp[-1])
