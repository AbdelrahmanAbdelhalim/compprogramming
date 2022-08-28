'''Problem Statement:
    You are given an m by n grid of integers representing a map of a dungeon. In this map:

    -1 represents a wall or an obstacle of some kind.
    0 represents a gate out of the dungeon.
    INF represents empty space.

For this question, let INF be 2^31 - 1 == 2147483647, which is the max value of the integer type in many programming languages.

Venturing into the dungeon is very dangerous, so you would like to know how close you are at each point in the dungeon to the exit. Given the map of the dungeon, return the same map, but for each empty space, that space is replaced by the number of steps it takes to reach any exit. If a space cannot reach the exit, that space remains INF.

Note that each step, you can move horizontally or vertically, but you cannot move pass a wall or an obstacle.
Input

    dungeon_map: a matrix of integer representing the dungeon map.

Output

A matrix of integer representing the dungeon map with the addition of distance to an exit for each empty space.
Examples
Example 1:

Input:

dungeon_map = [

  [INF, -1, 0, INF],

  [INF, INF, INF, -1],

  [INF, -1, INF, -1],

  [0, -1, INF, INF],

]

Output: [ [3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4], ]
This needs some good thinking.
Very good question. Need to examine the efficiency.
Solution roughly follows the solution suggested by algo monster
'''
from typing import List
from collections import deque

def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    def get_neighbors(dungeon_map, coords):
        row, col = coords
        row_offsets = [1, -1, 0 ,0]
        col_offsets = [0, 0, 1, -1]
        res = []
        for i in range(len(row_offsets)):
            new_row = row + row_offsets[i]
            new_col = col + col_offsets[i]
            if 0 <= new_row < len(dungeon_map) and 0 <= new_col < len(dungeon_map[0]):
                if dungeon_map[new_row][new_col] in [-1,0]:
                    continue
                res.append((new_row, new_col))
        return res
    
    def bfs(dungeon_map, stack):
        current_level = -1
        while(len(stack) > 0):
            current_level += 1
            for _ in range(len(stack)):
                node = stack.popleft()
                row, col = node
                if dungeon_map[row][col] < current_level:
                    continue
                else:
                    dungeon_map[row][col] = current_level
                    neighbors = get_neighbors(dungeon_map, node)
                    for neighbor in neighbors:
                        stack.append(neighbor)
    
    def traverse(dungeon_map):
        for i in range(len(dungeon_map)):
            for j in range(len(dungeon_map[0])):
                if dungeon_map[i][j] == 0:
                    stack = deque([(i,j)])
                    bfs(dungeon_map, stack)
    traverse(dungeon_map)
    return dungeon_map

