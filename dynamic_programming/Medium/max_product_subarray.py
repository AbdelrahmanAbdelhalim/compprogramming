'''Problem Statement:
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''@TODO: Write intuition behind solution
        Solution Result on leetcode:
           - Runtime: 100 ms, faster than 64.91% of Python3 online submissions.
           - Memory Usage: 14.4 MB, less than 78.79% of Python3 online submissions.
        '''
        if len(nums) == 0:
            return 0
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        for i in range(1, len(nums)):
            temp_max = max(min_so_far * nums[i], max_so_far * nums[i], nums[i])
            min_so_far = min(max_so_far * nums[i], min_so_far * nums[i], nums[i])
            max_so_far = temp_max
            result = max(max_so_far, result)
        return result
        
