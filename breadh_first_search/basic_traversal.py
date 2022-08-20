from typing import List
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> List[List[int]]:
    queue = deque([root])
    ans = []
    while len(queue) > 0:
        n = len(queue)
        level = []
        for i in range(n):
            parent = queue.popleft()
            level.append(parent.val)
            for child in [parent.left, parent.right]:
                if child is not None:
                    queue.append(child)
        ans.append(level)
    return ans

