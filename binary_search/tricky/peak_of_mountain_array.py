"""Problem Statement
A mountain array is defined as an array that

    has at least 3 elements
    has an element with the largest value called "peak", with index k. The array elements monotonically increase from the first element to A[k], and then monotonically decreases from A[k + 1] to the last element of the array. Thus creating a "mountain" of numbers.

That is, given A[0]<...<A[k-1]<A[k]>A[k+1]>...>A[n-1], we need to find the index k. Note that the peak element is neither the first nor the last element of the array.

Find the index of the peak element. Assume there is only one peak element.

Input: 0 1 2 3 2 1 0

Output: 3

Explanation: the largest element is 3 and its index is 3.
"""

"""Explanation
Similar to the other problem we look to find a criteria that would split the array into two halves of true and false.
The numbers in the case of this array are either descending or ascending. as long as we are ascending it means that
the answer is to the right of the midpoint or the midpoint itself. If we are descending it means that the answer is
on the left hand side of the midpoint. The easiest way to detect if we are ascending or descending is by checking
the midpoint against the value immediately before it. If it is larger that means we are ascending. If it is smaller
that means we are descending
"""

def peak_of_mountain_array(arr: List[int]) -> int:
    l = 0
    r = len(arr) - 1
    ans = -1
    while l <= r:
        mid = int((l+r)/2)
        if arr[mid] >= arr[mid - 1]:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

