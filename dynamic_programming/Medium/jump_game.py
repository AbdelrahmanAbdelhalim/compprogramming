class Solution:
    '''Initial solution
    Result: Time limit exceeded
    '''
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        dp = [0 for i in range(len(nums))]
        dp[-1] = 1
        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= len(nums) - 1:
                dp[i] = 1
            else:
                for k in range(nums[i]+1):
                    if dp[i+k] == 1:
                        dp[i] = 1
        return dp[0] == 1

class Solution:
    '''First optimization:
    Instead of the aggressive way of populating dp (Which exceeds the time
    limit for big numbers in the array). In the spirit of DP create a pointer for the target
    index that starts at the last index. If we are able to reach it then move the target index
    to the current index and run for smaller values. Note this is more of a greedy approach.
    And a good example to when greedy can outperform dp
    Performance from leetcode:
        - Runtime: 821 ms, faster than 29.41% of Python3 online submissions for Jump Game.
        - Memory Usage: 15.3 MB, less than 18.12% of Python3 online submissions for Jump Game.
    '''
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        dp = [0 for i in range(len(nums))]
        dp[-1] = 1
        target_index = len(nums)-1
        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= target_index:
                dp[i] = 1
                target_index = i
        return dp[0] == 1
                    
