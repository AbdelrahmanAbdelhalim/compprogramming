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
