# Graphs

## Tree with 0+ cycles

A tree is a connected acyclic graph.
A graph may contain cycle(s) and nodes could be disconnected.
A tree also contains n nodes and n-1 edges
There exists only 1 path between two nodes in a tree

## Graph terminlogies
Graph consists of vertices "Nodes" and edges.
Vertices are connected by edges.
Vertices connected by an edge are called neighbours and are adjacend
Edges can be unidirect or directed.
A path is a sequence of vertices. A cycle is a path that starts and ends at the same vertex
An undirected graph is connected if every vertex is joined by a path to another vertex
A graph is most commonly stored as a map of adjacency lists: for each vertex, store a list of its
neighbours
{
    1:[2,3],
    2:[1,3,4],
    3:[1,2],
    4:[2]
}

## BFS on graphs
Most interview problems focus on connected undirected graphs. The algorithms covered in bfs and dfs apply
to graphs as well. The only caveat is for cycles, in which case we keep the visited nodes in a data struc
with low retrieval complexity such as a hash set.

BFS Template:

    from collections import deque
    def bfs(root):
        stack = deque([root])
        visited = set([root])
        while len(stack > 0):
            node = stack.popleft()
            for neighbor in get_neighbors(node):  #get_neighbors fetches the neighboring nodes of the vertex
                if neighbor in visited:
                    continue
                stack.append(neighbor)
                visited.add(neighbor)

If we want to keep track of the level, we follow the same for tree traversal.
We can get the number of nodes in a level by looking at the length of the queue
from collections import deque


    def bfs(root):
        queue = deque([root])
        visited = set([root])
        level = 0
        while len(queue) > 0:
            n = len(queue) # get # of nodes in the current level
            for _ in range(n):
                node = queue.popleft()
                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            # increment level after we have processed all nodes of the level

            level += 1

## Depth First Search on Graphs
Similar to DFS, we just have to add visited to keep track of the visited nodes and use get_neighbors to 
get the next nodes to visit

DFS Template:

    def dfs(root,visited):
        for neighbor in get_neighbors(root):
            if neighbor in visited:
                continue
            visited.add(neighbor)
            dfs(neighbor, visited)

## BFS or DFS

If you have to just visited each node once without memory constraints then it doesn't matter

BFS is better at:
- Finding the shortest distance between two vertices
- Graph of unknown size

DFS is better at:
- Using less memory, BFS has to keep all the nodes in the queue and for wide graphs, this can get very large
- Finding nodes far away from the root

## Matrix as a graph

Very often graph problems are repsresented as matrices.
A matrix translates to a graph adjacency list
When we code the problem, we build the graph as we go

Nodes/vertices are represented as coordinatesof matrix entries

## Getting neighboring nodes
The shift here happens in the get_neighbors() function where we return
up to 8 neighboring nodes (if we allow diagonal searchnig) The common way of doing that is to store the offsets in the x and y as a permuation tablea nd to add them to the node's cooridnates to get the neighbors

    num_rows, num_cols = len(grid), len(grid - 1)
    def get_neighbors(coords) -> set:
        row, col = coords
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        res = []
        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
            res.append((neihbor_row, neighbor_col))
        return res

