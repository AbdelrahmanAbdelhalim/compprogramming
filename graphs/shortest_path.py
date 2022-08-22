from collections import deque
from typing import List

def shortest_path(graph: List[List[int]], a:int, b:int) -> int:
    def get_neighbors(node):
        return graph[node]

    stack = deque([a])
    visited = set([a])
    current_level = 0
    while len(stack) > 0:
        n = len(stack)
        for _ in range(n):
            node = stack.popleft()
            if node == b:
                return current_level
            neighbors = get_neighbors(node)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                stack.append(neighbor)
                visited.add(neighbor)
        current_level += 1
    return -1
