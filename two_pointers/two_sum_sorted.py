"""
Given an array of integers sorted in ascending order, 
find two numbers that add up to a given target. Return the indices of the two numbers in ascending order.
You can assume elements in the array are unique and there is only one solution.
Do this in O(n) time and with constant auxiliary space."""
from typing import List


# [1, 0, 2, 0, 0, 7]
from typing import List

def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    left = 0
    right = len(arr) - 1
    while right > left:
        if arr[right] + arr[left] == target:
            return [left,right]
        if arr[right] + arr[left] < target:
            left += 1
        if arr[right] + arr[left] > target:
            right -= 1
    return []

