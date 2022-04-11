class Solution:
    def rob_top_down(self, nums: List[int]) -> int:
        def solve(i: int):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[1],nums[0])
            if i not in mem:
                mem[i] = max(solve(i - 2) + nums[i], solve(i - 1))
            else:
                return mem[i]
        mem = {}
        return solve(len(nums)-1)
        
    def rob_bottom_up(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]
