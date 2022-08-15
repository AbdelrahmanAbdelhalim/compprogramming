'''The faster solution of imagining the tree
The other way is to have a binary include and not include tree
This solution utilises that the values are final results and
uses that fact to our advantage and uses them as nodes in the
search tree. Includes the empty set in the end. Or can
be appeneded in the beginning as the starting set of
all the other sets.
'''
from typing import List
def subsets(nums: List[int]) -> List[List[int]]:
    def traverse(last_index, nums, current_path, ans): 
        for i in range(last_index, len(nums)):
            current_path.append(nums[i])
            ans.append(current_path.copy())
            traverse(i + 1, nums, current_path, ans)
            current_path.pop()
        
    ans = []
    current_path = []
    traverse(0, nums, current_path, ans)
    ans.append([])
    return ans

