'''Problem Statement
For this problem, given a list of tasks and a list of requirements, compute a sequence of tasks that can be performed, such that we complete every task once while satisfying all the requirements.

Each requirement will be in the form of a list [a, b], where task a needs to be completed first before task b can be completed,

There is guaranteed to be a solution.
Examples
Example 1
Input:

tasks = ["a", "b", "c", "d"]

requirements = [["a", "b"], ["c", "b"], ["b", "d"]]

Output: ["a", "c", "b", "d"]
'''
from typing import List
from collections import deque

def task_scheduling(tasks: List[str], requirements: List[List[str]]) -> List[str]:
    def build_graph(tasks, requirements):
        graph = {}
        for task in tasks:
            graph[task] = []
        for requirement in requirements:
            graph[requirement[0]].append(requirement[1])
        return graph


    def build_counts(graph):
        counts = {node: 0 for node in graph}
        for node in graph:
            for child in graph[node]:
                counts[child] = counts[child] + 1
        return counts

    def topo_sort(graph, counts):
        stack = deque()
        res = []
        for node in counts:
            if counts[node] == 0:
                stack.append(node)
        while len(stack) > 0:
            node = stack.popleft()
            res.append(node)
            for child in graph[node]:
                counts[child] = counts[child] - 1
                if counts[child] == 0:
                    stack.append(child)
        if len(res) == len(graph):
            return res
        return -1

    graph = build_graph(tasks, requirements)
    counts = build_counts(graph)
    return topo_sort(graph, counts)

