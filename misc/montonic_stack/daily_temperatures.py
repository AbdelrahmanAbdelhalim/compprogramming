"""Problem Statement
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
Examples
Example 1:
Input: [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
Note:

The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""

# So far it has been common to store the indices of the elements instead of their values in the stack since the values can be obtained from the input array at any time

from typing import List

def daily_temperatures(t: List[int]) -> List[int]:
    stack = []
    ans = [0 for i in range(len(t))]
    
    for i in range(len(t)):
        temp = t[i]
        while stack and t[stack[-1]] < temp:
            ans[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return ans
