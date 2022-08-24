'''Problem Statement
In computer graphics, an uncompressed raster image is presented as a matrix of numbers. Each entry of the matrix represents the color of a pixel. A flood fill algorithm takes a coordinate r, c and a replacement color, and replaces all pixels connected to r, c that have the same color (i.e., the pixels connected to the given coordinate with of same color and all the other pixels connected to the those pixels of the same color) with the replacement color. (e.g. MS-Paint's paint bucket tool).
Input

    r: row
    c: column
    replacement: replacement color
    image: an 2D array of integers representing the image

Output

the replaced image
'''

from typing import List
from collections import deque
def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    num_rows, num_cols = len(image), len(image[0])
    def get_neighbors(coords, color, image):
        row, col = coords
        row_offsets = [0,1,-1]
        column_offsets = [0,1,-1]
        res = []
        for row_offset in row_offsets:
            for column_offset in column_offsets:
                new_row_coord = row + row_offset
                new_col_coord = col + column_offset        
                if 0 <= new_row_coord < num_rows and 0<= new_col_coord < num_cols:
                    if image[new_row_coord][new_col_coord] == color:
                        res.append((new_row_coord, new_col_coord))
        return res
     
    def bfs(coords, color, image):
        stack = deque([coords])
        color_to_replace = image[coords[0]][coords[1]]
        while len(stack) > 0:
            for _ in range(len(stack)):
                node = stack.popleft()
                neighbors = get_neighbors(node, color_to_replace, image)
                for neighbor in neighbors :
                    stack.append(neighbor)
                for row, col in neighbors :
                    image[row][col] = color
    
        return image
    image = bfs((r,c), replacement, image)
    return image

