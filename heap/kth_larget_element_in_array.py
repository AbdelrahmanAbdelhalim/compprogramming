from typing import List
import heapq

def find_kth_largest(nums: List[int], k: int) -> int:
    nums = [-x for x in nums]
    ans = -1
    heapq.heapify(nums)
    for i in range(k):
        ans = (-1 * heapq.heappop(nums))
    return ans

