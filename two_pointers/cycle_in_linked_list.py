"""Problem Statement
Given a linked list with potentially a loop, determine whether the linked list from the first node contains a cycle in it. For bonus points, do this with constant space.
"""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def has_cycle(nodes: Node) -> bool:
    tortoise, hare = nodes, nodes
    while hare != None:
        hare = hare.next
        if hare is None:
            return False
        hare = hare.next
        tortoise = tortoise.next
        if hare == tortoise:
            return True
