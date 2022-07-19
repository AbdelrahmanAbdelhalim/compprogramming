"""Problem Statement
A sorted array of unique integers was rotated at an unknown pivot. For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20]. Find the index of the minimum element in this array. All the numbers are unique.

Input: [30, 40, 50, 10, 20]

Output: 3

Explanation: the smallest element is 10 and its index is 3.

Input: [3, 5, 7, 11, 13, 17, 19, 2]

Output: 7
"""

"""
This is where the idea of finding the boundary really shines. Also note that the elements need to be unique for this solution to work.
We opt to find a criteria that would set one part of the array to true and the other to false. Then the problem becomes finding that
boundary similar to all the binary searching that we have done before. The way to think about splitting the array is picking a number
in the array (in our case was the last element). The array is split into an ascending and descending parts. As long as the middle element
is smaller than the last element that means we are ascending and the answer will be in the left half of the array. If the element is bigger
that we means that we descended between the midpoint and the last element which means the answer is somewhere on the right hand side of the
split.
"""

from typing import List
def find_min_rotated(arr: List[int]) -> int:
    l = 0
    r = len(arr) - 1
    ans = -1
    while l <= r:
        mid = int((l+r)/2)
        if arr[mid] <= arr[-1]:
            ans = mid
            r = mid - 1
        elif arr[mid] > arr[-1]:
            l = mid + 1
    return ans

