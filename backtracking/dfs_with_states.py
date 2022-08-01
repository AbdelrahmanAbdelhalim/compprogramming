'''Problem Statement
Given a ternary tree (each node of the tree has at most three children), find all root-to-leaf paths.
'''
from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> List[str]:
    def traverse_tree(root, path_so_far, ans):
        if len(path_so_far) == 0:
            path_so_far.append(f'{root.val}')
        else:
            path_so_far.append(f'->{root.val}')
        if not root.children:
            ans.append(''.join(path_so_far))
        else:
            for child in root.children:
                traverse_tree(child, path_so_far, ans)
        path_so_far.pop()
    ans = []
    path_so_far = []
    traverse_tree(root,path_so_far,ans)
    return ans
