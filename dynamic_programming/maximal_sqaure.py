class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        dp = [[0 for i in range(cols+1)] for i in range(rows+1)]
        max_len = 0
        for i in range(1,(rows+1)):
            for j in range(1,(cols+1)):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(min(dp[i-1][j],dp[i][j-1]),dp[i-1][j-1]) + 1
                max_len = max(max_len, dp[i][j])
        return max_len * max_len
