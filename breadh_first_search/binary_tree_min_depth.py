from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_min_depth(root: Node) -> int:
    current_depth = -1
    stack = deque([root])
    while len(stack) > 0:
        current_depth += 1
        for _ in range(len(stack)):
            node = stack.popleft()
            if not node.left and not node.right:
                return current_depth
            for i in [node.left, node.right]:
                if i:
                    stack.append(i)
    return current_depth
