from typing import List
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_right_side_view(root: Node) -> List[int]:
    ans = []
    stack = deque([root])
    while len(stack) > 0:
        current_level = []
        for _ in range(len(stack)):
            node = stack.popleft()
            current_level.append(node)
            for i in [node.left, node.right]:
                if i:
                    stack.append(i)
        right_most_node = current_level.pop()
        ans.append(right_most_node.val)
    return ans

