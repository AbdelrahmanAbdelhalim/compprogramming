from typing import List
ans = set()
memo = {}

# Top Down solution
def knapsack_weight_only(weights: List[int]) -> List[int]:
    def traverse(weights, ssf, depth, md):
        if depth == md:
            ans.add(ssf)
            return
        if memo.get((depth, ssf)):
            return
        traverse(weights, ssf + weights[depth], depth + 1, md)
        traverse(weights, ssf, depth + 1, md)
        memo[(depth, ssf)] = True
        
    traverse(weights, 0, 0, len(weights))
    return list(ans)


# Bottom up solution (all me baby)

from typing import List
ans = set()
memo = {}

def knapsack_weight_only(weights: List[int]) -> List[int]:
    dp = [set() for i in range(len(weights) + 1)]
    dp[0].add(0)
    for i in range(len(weights)):
        for ssf in dp[i]:
            dp[i + 1].add(ssf + weights[i])
            dp[i + 1].add(ssf)
    return list(dp[-1])


