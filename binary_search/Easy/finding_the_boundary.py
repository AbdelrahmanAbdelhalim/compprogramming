"""Problem Statement: An array of boolean values is divided into two sections; the left section consists of all false and the right section consists of all true. Find the boundary of the right section, i.e. the index of the first true element. If there is no true element, return -1.

Input: arr = [false, false, true, true, true]

Output: 2

Explanation: first true's index is 2.

"""

"""First solution idea (Done by me)
For this solution I opted for not discarding the mid element and keeping it in range if it is true. The edge case that needs to be handled (as in
the if statement below) is when l == r. In that case mid == l == r and if it is true r would remain the same (since we keep it in range). Therefore,
we will be stuck forever and we need that additional check.
"""
from typing import List

def find_boundary(arr: List[bool]) -> int:
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = int((l+r)/2)
        if l == r:
            if arr[mid]:
                return mid
            else:
                return -1
        if arr[mid]:
            r = mid
        if not arr[mid]:
            l = mid + 1
    return -1

"""Second solution (From Algomonsger)
In this solution instead of keeping mid element in range and adding a check when l == r. We opt to store mid if it is true in its own
variable. That way if mid - 1 is false, we won't miss out on the index of the last true that we were able to find. Initializing the 
variable that we store the solution in to -1 gurantees that if the loop terminates without finding a true would return -1 as expected
"""
def find_boundary_2(arr: List[bool]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index
