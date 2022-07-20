# Introduction to Tree data structure

Trees are composed of nodes connected by edges.

Each node:
    - Can have zero or more child nodes
    - Must be connected to exactly one parent node except for the root node.
Each tree has only one root node. These constraints mean that there are no cycles or loops

## Terminologies related to trees:
    - Internal node: everyn ode in a tree which is not a root node
    - Leaf node: every node that has no children
    - Ancestor: All the nodes that are between the path from the root to the current node
    - Descendent: All the nodes that are reachable from the current node when moving down the tree.
    - Level: Level of a node is the number of ancestors between the node and the root of the tree
    - Depth: Depth of a node is the number of edges on the path from the root to that node
    - Height: Height of a node is the number of edges on the longest path from that node to a leaf.

## Types of a tree

### Binary Tree
An n-ary tree is a tree where each node has no more than n children. A binary tree is a type of n-nary tree where n = 2. Every node in a binary tree has 0 to 2 children.

### Binary search tree
A binary search tree is a tree where:
    - All left descendents of the node are smaller than the node
    - All right descendents of the node are bigger than the node

## Balanced binary tree
- Every node in a balanced binary tree follows the condition: The height difference of the left and right subtree of the node is no more than 1.
- Searching, insertion, deletion in a balanced binary tree takes O(log n) instead of O(n) in an unbalanced binary tree.
- Common types of balanced binary trees are red-black trees and AVL trees.

## Tree Traversal
- In-order traversal: left, node, right
- Pre-order traversal: node, left, right
- Post-order traversal: left, right, node


