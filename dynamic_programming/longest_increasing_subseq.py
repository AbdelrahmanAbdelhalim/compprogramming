# Bottom up solution. need to do top down
def longest_sub_len(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    dp = [math.inf for i in range(len(nums))]         
    dp[0] = 1
    for i in range(1, len(nums)):
        mx = -math.inf
        for j in range(i):
            if nums[i] > nums[j]:
                mx = max(dp[j], mx)
        if mx > 0:
            dp[i] = mx + 1
        else:
            dp[i] = 1
               
    return max(dp)
