# Depth First Search
Searching a tree as deep as possible. When a target is not found, we re-trace our steps back and go deep again.
pre-order traversal is depth first search

IMPORTANT NOTE: Being able to visualize recursion and call stack of a DFS cunrtion is extremely important.

Backtracking and divide and conquer can be seen from how depth first search functions. The action of retracing steps is called backtracking. Backtracking and DGS are similar concepts and essentialy the same thing. To make the distinction it could be said that backtracking is the concept of retracing and DFS is the algorithm that performs it.
Backtracking is usually placed under combinatorial problems in many computer science textbook and that is the
approach that will be taken with this study.

In dfs we have two recursive call for each branch of the tree and return based on the result from the recursive
call. So this is also a divide and conquer algorithm.

## When to use DFS

DFS is a pre-order traversal:
    - Traverse and find/create/modify/delete node
    - Traverse with return value

Combinatorial problems:
DFS/backtracking and combinatorial problems are a 'match made in heaven'. Combinatorial problems boil down
to searching in trees
    - How many ways there are to arrange something
    - Find all possible combinations of
    - Find all solutions to a puzzle

Graph:
Trees are special graphs that have no cycles. We can still use DFS with graphs with cycles, we will need however to record the nodes that we have visited and avoid re-visiting them again.
    - Find path from point A to point B
    - Find connected components
    - Detect Cycles

