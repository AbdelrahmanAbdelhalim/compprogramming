"""Problem Statement
Given an integer, find its square root without using the built-in square root function. Only return the integer part (truncate the decimals).

Input: 16

Output: 4

Input: 8

Output: 2

Explanation: square root of 8 is 2.83..., return integer part 2
"""

"""My solution
The solution to this problem boils down to finding the latest value i where i^2 < n. And effictively can be done with binary search
"""
def square_root(n: int) -> int:
    l = 0
    r = n
    ans = 0
    while l <= r:
        mid = int((l+r)/2)
        if mid * mid == n:
            return mid
        if mid * mid < n:
            ans = mid
            l = mid + 1
        if mid * mid > n:
            r = mid - 1
    return ans
