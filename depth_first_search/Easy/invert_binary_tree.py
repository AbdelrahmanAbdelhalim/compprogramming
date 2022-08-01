'''Problem Statement
Given a binary tree, invert it and return the new value. You may invert it in-place.

To "invert" a binary tree, switch the left subtree and the right subtree, and invert them both. Inverting an empty tree does nothing.
Input

    tree: a binary tree that needs to be inverted.

Output

The inverted binary tree.
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(tree: Node) -> Node:
    def invert_helper(root):
        if not root:
            return
        temp_reference = root.left
        root.left = root.right
        root.right = temp_reference
        invert_helper(root.left)
        invert_helper(root.right)
    invert_helper(tree)
    return tree

'''
Improvement on the solution
Can be done in less space by constructing a new node and switching its children away and returning it
'''

