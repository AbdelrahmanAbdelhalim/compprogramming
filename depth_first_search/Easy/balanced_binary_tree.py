'''Problem Statement
A balanced binary tree is defined as a tree such that either it is an empty tree, or both its subtree are balanced and has a height difference of at most 1.
In that case, given a binary tree, determine if it's balanced.
Parameter
    tree: A binary tree.
Result
    A boolean representing whether the tree given is balanced.

'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(tree: Node) -> bool:
    return abs(max_depth(tree.left, 0) - max_depth(tree.right, 0)) <= 1

def max_depth(node, current_depth):
    if not node:
        return 0
    depth_left = max_depth(node.left, current_depth)
    depth_right = max_depth(node.right, current_depth)
    return max(depth_left, depth_right) + 1

# this function build a tree from input
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    res = is_balanced(tree)
    print('true' if res else 'false')
