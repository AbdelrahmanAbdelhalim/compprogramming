class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''Performance result from leetcode:
                - Runtime: 2891 ms, faster than 19.26% of Python3 submissions.
                - Memory Usage: 14.2 MB, less than 75.25% of Python3 submissions
            logic behind solution:
                dp[i] represents the minimum number of coins to make i amount.
                We start with the base case of i = 0, where we need 0 coins to do that.
                From there we see where each coin takes us. For example: if we have a
                coin of value x, then from i = 0 we can get to i = x (0 + x) in one step.
                We do that for all our coins while keeping the minimum number in dp[i+x]
                The final solution should be in dp[-1]. if dp[-1] == math.inf then we were
                unable to reach that amount from the coins that we have.
        '''
        if amount <= 0:
            return 0
        import math
        dp = [math.inf for i in range(amount+1)]
        dp[0] = 0
        for i in range(len(dp)):
            for j in coins:
                if i + j < len(dp):
                    dp[i+j] = min(dp[i] + 1, dp[i+j])
        if dp[-1] == math.inf:
            return -1
        else:
            return(dp[-1])
