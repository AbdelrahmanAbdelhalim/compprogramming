"""Problem Statement
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
"""

def sumNumbers(self, root: Optional[TreeNode]) -> int:
    ans = [] # Could do with a non local variable but I could not be asked to look up how to do it
    def traverse(root, ssf, ans):
        if not root:
            return
        if not root.left and not root.right:
            ans.append(ssf * 10 + root.val)
            return

        ssf *= 10
        ssf += root.val
        traverse(root.left, ssf, ans)
        traverse(root.right, ssf, ans)

    traverse(root, 0 , ans)
    return sum(ans)
