"""Important Note. This problem is on the difficult side.
Get back to solving this when you are revising again.

"""
"""
No explanation provided for now until you solve it again
"""
def possible(weights, d, cap):
    capacity = cap
    required_days = 1
    index = 0
    while(index < len(weights)):
        if weights[index] <= capacity:
            capacity -= weights[index]
            index += 1
        else:
            capacity = cap
            required_days += 1
    return required_days <= d

def min_max_weight(weights: List[int], d: int) -> int:
    l = max(weights)
    r = sum(weights)
    ans = 0
    while l <= r:
        mid = int((l+r)/2)
        if possible(weights, d, mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

