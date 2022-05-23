class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        if len(text1) <=0 or len(text2) <=0:
            return 0
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = max((dp[i-1][j-1] + 1),dp[i][j])
        return dp[m][n]
