from typing import List
from collections import deque

def count_number_of_islands(grid: List[List[int]]) -> int:
    def get_neighbors(coord, grid):
        row, col = coord[0], coord[1]
        row_offsets = [1, -1, 0, 0]
        col_offsets = [0, 0, 1, -1]
        res = []
        for i in range(len(row_offsets)):
            new_row = row + row_offsets[i]
            new_col = col + col_offsets[i]
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                res.append((new_row,new_col))
        return res
    
    def bfs(grid, row, col):
        stack = deque([(row, col)])
        while len(stack) > 0:
            current_coords = stack.pop()
            row_coord = current_coords[0]
            col_coord = current_coords[1]
            if grid[row_coord][col_coord] == 1:
                grid[row_coord][col_coord] = -1
                neighbors = get_neighbors(current_coords, grid)
                for neighbor in neighbors:
                    stack.append(neighbor)
    
    def traverse(grid):
        row_limit = len(grid)
        col_limit = len(grid[0])
        ans = 0
        for i in range(row_limit):
            for j in range(col_limit):
                if grid[i][j] == 1:
                    bfs(grid, i , j)
                    ans += 1
        return ans

    return traverse(grid)

