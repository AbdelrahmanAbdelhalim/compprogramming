'''
Problem Statement:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array
'''
class Solution:
    '''
    Intuition behind solution: We start the problem at len(nums) = 1
    where the maximum sum of the array is nums[0]. This is the solution
    to our first subproblem. Then for every consequent element we have two
    choices: we either restart the array at that element or we take that 
    element as part of the solution subarray. The only time where we restart
    the array at index i is when nums[i] is greater than nums[i] + dp[i-1]
    where we get no benefit of including the previous maximum sum at all.
    Otherwise we should always include the element in the subarray. We can't
    skip the element if it reduces the total because that means we won't be
    able to include any elements afterwards since the array needs to be
    contiguous. The solution to the problem at the end is in max(dp)
    '''
    def top_down_solution(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], (dp[i-1] + nums[i]))
        return max(dp)
    
