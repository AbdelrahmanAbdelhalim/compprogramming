"""Problem Statement
Given a sorted list of numbers, remove duplicates and return the new length. You must do this in-place and without using extra memory.

Input: [0, 0, 1, 1, 1, 2, 2].

Output: 3.
"""

from typing import List

def remove_duplicates(arr: List[int]) -> int:
    slow = 0
    for i in range(len(arr)):
        if arr[i] == arr[slow]:
            continue
        slow += 1
        arr[slow] = arr[i]
    return slow + 1

