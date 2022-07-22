'''Problem Statement
In a binary tree, we define a node "visible" when no node on the root-to-itself path (inclusive) has a greater value. The root is always "visible" since there are no other nodes between the root and itself. Given a binary tree, count the number of "visible" nodes.
'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node_non_local_variable(root: Node) -> int:
    import math
    ans = 0
    def find_visible_nodes(root: Node, biggest_so_far):
        nonlocal ans
        if root:
            if root.val >= biggest_so_far:
                ans += 1
                biggest_so_far = root.val
            for i in [root.left, root.right]:
                find_visible_nodes(i, biggest_so_far)
    find_visible_nodes(root,-math.inf)

def visible_tree_node(root: Node) -> int:
    import math
    def count_visible_nodes(root, biggest_so_far):
        if not root:
            return 0
        biggest_check = 0
        if root.val >= biggest_so_far:
            biggest_so_far = root.val
            biggest_check = 1
        return biggest_check + sum(count_visible_nodes(i,biggest_so_far) for i in [root.left, root.right])
    ans = count_visible_nodes(root, -math.inf)
    return ans

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
    res = visible_tree_node(root)
    print(res)

