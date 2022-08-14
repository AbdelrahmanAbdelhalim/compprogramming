'''
Traverse the tree normally as you would. However, don't consider the
candidates that you have already tried out.
This needs careful consideration again since I can't really wrap
my head around how it works yet.
'''
from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    def traverse(remainder_sum, path_so_far, candidates, last_candidate_index):
        if remainder_sum == 0:
            ans.append(path_so_far.copy())
        if remainder_sum < 0:
            return
        for i in range(last_candidate_index, len(candidates)):
            path_so_far.append(candidates[i])
            traverse(remainder_sum - candidates[i], path_so_far, candidates, i)
            path_so_far.pop()
    ans = []
    traverse(target, [], candidates, 0)
    return ans
