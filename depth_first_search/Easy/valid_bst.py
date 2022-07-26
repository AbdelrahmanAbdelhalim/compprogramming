'''Problem Statement
A binary search tree is a binary tree with the property that any of its node's value is greater than or equal to any node in its left subtree and less than or equal to any node's value in its right subtree.

Given a binary tree, determine whether it is a binary search tree.
'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root: Node) -> bool:
    import math
    def validate_bst(root, lower_bound, upper_bound):
        if not root:
            return True
        if root.val >= lower_bound and root.val <= upper_bound:
            left_subtree_valid = validate_bst(root.left, lower_bound, root.val)
            right_subtree_valid = validate_bst(root.right, root.val, upper_bound)
            return left_subtree_valid and right_subtree_valid
        else:
            return False
    return validate_bst(root, -math.inf, math.inf)

# this function build a tree from input
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = valid_bst(root)
    print('true' if res else 'false')
