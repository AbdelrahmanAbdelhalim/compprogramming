class Solution:
    def jump(self, nums: List[int]) -> int:
        '''Solution performance on leetcode:
            Time limit exceeded. O(N^2) Dynamic programming algorithm
            We need to look for greedy
            Correct solution. Slow tho.

            Greedy algorithm is a nice and tricky way of solving the problem.
            The thinking around the greedy algorithm is:
                - Think of the jumps as the upper bound of the array that you can jump to
                - If you pick the biggest number you allow youself to look at a bigger range
                  of options to choose greedily from. The optimal solution that investiagtes all
                  paths you will end up with less options and therefore the greedy algorithm works
                  better
        '''
        if len(nums) <= 0:
            return 1
        import math
        dp = [math.inf for i in range(len(nums))]
        dp[0] = 0
        for i in range(1,len(nums)):
            for k in range(i):
                if nums[k] + k >= i:
                    dp[i] = min(dp[i], dp[k] + 1)
        return dp[-1]

#  Note: the greedy solution achieves better results than dynamic programming for this problem. The proof is a bit
#        complicated however it is a todo.
