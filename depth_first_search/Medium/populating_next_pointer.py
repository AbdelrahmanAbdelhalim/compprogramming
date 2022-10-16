"""
"""

class Solution:
    """Tree Level Travesal
    """
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        from collections import deque
        queue = deque([root])
        while len(queue) > 0:
            previous_node = None
            for _ in range(len(queue)):
                current_node = queue.popleft()
                if previous_node:
                    previous_node.next = current_node
                previous_node = current_node
                if current_node:
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
        return root
                        
