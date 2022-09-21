"""Problem Statement
Given an array of integers and an integer target, find a subarray that sums to target and return the start and end indices of the subarray.

Input: arr: 1 -20 -3 30 5 4 target: 7

Output: 1 4

Explanation: -20 - 3 + 30 = 7. The indices for subarray [-20,-3,30] is 1 and 4 (right exclusive).
"""

from sys import prefix
from typing import List

def subarray_sum(arr: List[int], target: int) -> List[int]:
    prefix_sums = {}
    sum_so_far = 0
    for i in range(len(arr)):
        sum_so_far += arr[i]
        prefix_sums[sum_so_far] = i
    
    for i in prefix_sums:
        to_find = i - target
        if to_find == 0:
            idx = prefix_sums[i]
            ret = [0, idx + 1]
            return ret
        if prefix_sums.get(to_find) is not None:
            first_index = prefix_sums[to_find]
            second_index = prefix_sums[i]
            ret = [second_index, first_index]
            ret.sort()
            ret[0] += 1
            ret[1] += 1
            return ret
    return []

