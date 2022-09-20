"""Problem Statement
Find the middle node of a linked list.

Input: 0 1 2 3 4

Output: 2

If the number of nodes is even, then return the second middle node.
"""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middle_of_linked_list(head: Node) -> int:
    slow, fast = head, head
    while fast is not None:
        fast = fast.next
        if fast is None:
            return slow.val
        fast = fast.next
        slow = slow.next
    return slow.val

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None: return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

