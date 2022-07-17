"""Author: @AbdelrahmanAbdelhalim github
"""

from typing import List

def binary_search(arr: List[int], target: int) -> int:
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = int((r+l)/2)
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            r = mid - 1
        elif target > arr[mid]:
            l = mid + 1
    return -1

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = binary_search(arr, target)
    print(res)
