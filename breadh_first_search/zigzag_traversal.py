from typing import List
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zig_zag_traversal(root: Node) -> List[List[int]]:
    stack = deque([root])
    ans = []
    reverse = False
    while len(stack) > 0:
        current_path = []
        for _ in range(len(stack)):
            node = stack.popleft()
            current_path.append(node.val)
            for i in [node.left, node.right]:
                if i:
                    stack.append(i)
        if reverse:
            current_path.reverse()
        reverse = not reverse
        ans.append(current_path)       
    return ans
