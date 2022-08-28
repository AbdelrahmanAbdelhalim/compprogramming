def get_knight_shortest_path(x: int, y: int) -> int:
    def get_neighbors(coords, visited):
        row_offsets = [-2, -2, -1, -1, 1, 1, 2, 2]
        col_offsets = [-1, 1, -2, 2, -2, 2, -1 ,1]
        row_coord = coords[0]
        col_coord = coords[1]
        res = []
        for i in range(len(row_offsets)):
            new_row = row_coord + row_offsets[i]
            new_col = col_coord + col_offsets[i]
            if (new_row, new_col) in visited:
                continue
            res.append((new_row, new_col))
        return res
        
    def bfs(x, y):
        stack = deque([(0,0)])
        visited = set([(0,0)])
        current_level = -1
        while len(stack) > 0:
            current_level += 1
            for _ in range(len(stack)):
                node = stack.popleft()
                row = node[0]
                col = node[1]
                if row == x and col == y:
                    return current_level
                neighbors = get_neighbors((row,col), visited)
                for neighbor in neighbors:
                    neighbor_row = neighbor
                    stack.append(neighbor)
    return bfs(x, y)
