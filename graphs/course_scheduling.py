"""Problem Statement
There are a total of n courses a student has to take, numbered from 0 to n-1. A course may have prerequisites. The "depends on" relationship is expressed as a pair of numbers. For example, [0, 1] means you need to take course 1 before taking course 0. Given n and the list of prerequisites, decide if it is possible to take all the courses.

"""

from random import paretovariate
from typing import List
from collections import deque

def build_graph(n, prerequisites):
    graph = {i: [] for i in range(n)}
    for depend in prerequisites:
        parent = depend[0]
        child = depend[1]
        graph[parent].append(child)
    return graph


def get_parent_counts(n, graph):
    parent_counts = {i:0 for i in range(n)}
    for node in graph:
        for child in graph[node]:
            parent_counts[child] += 1
    return parent_counts

def is_valid_course_schedule(n: int, prerequisites: List[List[int]]) -> bool:
    graph = build_graph(n , prerequisites)
    parent_counts = get_parent_counts(n, graph)
    stack = deque()
    courses_completed = 0
    for node in parent_counts:
        if parent_counts[node] == 0:
            stack.append(node)
    while(len(stack) > 0):
        node = stack.pop()
        courses_completed += 1
        for child in graph[node]:
            parent_counts[child] -= 1
            if parent_counts[child] == 0:
                stack.append(child)
            
    
    return courses_completed == n

