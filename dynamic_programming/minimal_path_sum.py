# Tabular solution
from typing import List
import math

def min_path_sum(grid: List[List[int]]) -> int:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 and j == 0:
                continue
            above = math.inf if i - 1 < 0 else grid[i - 1][j]
            nxt = math.inf if j - 1 < 0 else grid[i][j - 1]
            grid[i][j] = min(above + grid[i][j], nxt + grid[i][j])
            
    return grid[-1][-1]
