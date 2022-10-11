# Top Down Solution
def can_partition(nums: List[int]) -> bool:
    target = sum(nums)
    if target % 2 != 0:
        return False
    memo = [[-1 for i in range(len(nums))] for i in range(target)]
    target /= 2
    def traverse(depth, ssf, target, nums, memo):
        if depth == len(nums):
            if ssf != target:
                return False
        if ssf == target:
            return True
        
        if memo[ssf][depth] != -1:
            return memo[ssf][depth]
        incl = traverse(depth + 1, ssf + nums[depth], target, nums, memo)
        excl = traverse(depth + 1, ssf, target, nums, memo)
        memo[ssf][depth] = incl or excl
        return incl or excl
    ans = traverse(0, 0, target, nums, memo)
    return ans
