class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for i in range(amount + 1)]
        dp[0] = 1
        for j in coins:
            for i in range(j, len(dp)):
                dp[i] = dp[i - j] + dp[i]
        return dp[-1]
        # The reason why you calculate it in a retro way is because we would like to take into account
        # the state from which we came. We can't calculate that if we calculate feed forward.
