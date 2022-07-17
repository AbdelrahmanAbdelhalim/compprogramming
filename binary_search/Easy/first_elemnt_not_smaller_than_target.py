"""Problem Statement
Given an array of integers sorted in increasing order and a target, find the index of the first element in the array that is larger than or equal to the target. Assume that it is guaranteed to find a satisfying number.

Input:

    arr = [1, 3, 3, 5, 8, 8, 10]
    target = 2

Output: 1

Explanation: the first element larger than 2 is 3 which has index 1.

Input:

    arr = [2, 3, 5, 7, 11, 13, 17, 19]
    target = 6

Output: 3

Explanation: the first element larger than 6 is 7 which has index 3.

"""

"""First idea found by me
Very easy to find
"""
from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    l =  0
    r = len(arr) - 1
    ans = 0
    while l <= r:
        mid = int((l+r)/2)
        if arr[mid] == target:
            ans = mid
            r = mid - 1
        elif arr[mid] > target:
            ans = mid
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
    return ans

# A small note on my solution. The condition for arr[mid] == target and arr[mid] > target is redundant and can be shrunk to the same if statement.
