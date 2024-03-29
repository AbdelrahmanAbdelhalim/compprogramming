#Graphs

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


## Topological sort
Topological sort is the ordering of a directed graph where every node appears in the ordering before all the nodes it points to

Graphs with cycles do not have a topological sort

### Kahn's Algorithm
Very similar to breadth first search
The idea is -> given a directed graph: is there a way of removing a node such that each time we remove a node we guarantee that no other nodes point to that particular node ?
Systematically remove one node at a time , each time removing a node that noother node points to.

- Initialize a hashmap of node to parent count
- Go through the nodes, count how many parents each node has
- Push the node with 0 parents into the queue
- Pop each node from the queue, subtract 1 from the parent count of each node it points to
- If a node's parent count drops to 0 then push it into the queue
- Repeate until the queue is empty. If the queue is not empty, there is maybe a cycle (or you are an idiot)

Topological sort algorithm is very similar to BFS. The main difference is that we only push nodes with 0 parents into the queue in toplogical sort whereas in BFS we push all neighboring nodes in the queue.

Similar to BFS we keep things short and clear. Two functions `count_parents()` and `topo_sort()`

    from collections import deque
    def count_parents(graph):
        counts = {node: 0 for node in graph}
        for parent in graph:
            for node in graph[parent]:
                counts[node] += 1
        return counts

    def topo_sort(graph):
        res = []
        q = deque()
        counts = count_parents(graph)
        for node in counts:
        if counts[node] == 0:
            q.append(node)
        while len(q) >0:
            node = q.popleft()
            res.append(node)
            for child in graph[node]:
                counts[child] -= 1
                if counts[child] == 0:
                    q.append(child)
        return res if len(graph) == len(res) else None
        
The algorithm is very similar to BFS. Except we initialize the queue with
nodes that have 0 parents

## Dijkstra's Algorithm
Working with weighted graphs where the edges carry values.

### Shortest-Path Faster Algorithm (SPFA)
Can be thought of as a BFS variant. Instead of checking wehter or not the neighbor node has been visited we instead see if we can improve our distance by checking the neighbor nodes.

## Dijkstra's Algorithm
Uses a priority queue. To store nodes by the distance from the root node. That way every time we pop a node, we konw that the distance is the shortest distance from our source node to the node. And we update the distances of the neighbors of the node by decrease_priority to make sure the distances of other nodes in the priority queue is the shortedst from the source node. (Needs another look, forgot how it works)

## Uniform Cost Search
In Dijkstra's algorithm, we add all vertices to the priority queue at the beginning. This can be difficult if the graph is very large. Uniform cost search algorithm is a variant of Dijkstra's. We start with the priority queue containing only the root node and add new vertices as we check the neighbors

## Minimum Spanning Tree
Minimum spanning tree is a tree for a given graph with overall minimum weight generated from a graph.
