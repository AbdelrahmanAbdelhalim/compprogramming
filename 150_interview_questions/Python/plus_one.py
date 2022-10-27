"""Problem Statement
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        carry = True
        counter = len(nums) - 1
        while counter >= 0:
            if nums[counter] != 9:
                carry = False
                nums[counter] += 1
                return nums
            else:
                nums[counter] = 0
            counter -= 1
        if carry:
            ans = [0 for i in range(len(nums) + 1)]
            ans[0] = 1
            return ans
        return nums
