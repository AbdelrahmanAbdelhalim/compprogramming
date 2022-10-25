"""Problem Statement
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.
Examples
Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation:

The first 1's next greater number is 2;

The number 2 can't find next greater number;

The second 1's next greater number needs to search circularly, which is also 2.
"""

# Same as temperatures question but with two passes instead
from typing import List

def next_greater_elements(nums: List[int]) -> List[int]:
    ans = [-1 for i in range(len(nums))]
    stack = []
    for i in range(2):
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                if ans[stack[-1]] == -1:
                    ans[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
    return ans

