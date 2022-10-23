# Advanced Data Structures

## Disjiont set union data structure
We are motivated by the following problem. Suppose we have sets of elements and we are asked to check if a certain element belongs to a particular set. In addition, we want to have our data structure support updates as well, through merging two sets into one set.
- We want to be able to query for the set id of a given node (find operation)
- We want to merge two disjoint sets into one set (union operation)

We can imagine the disjoint set data structure as a series of trees such that a particular element within a tree belons solely to that set and no other set.
The elements are the particular nodes of the tree that belong to that set and we nominate a particular node to be the parent of all the nodes which will act as an identifier.
If two nodes share the same parent then they belong to the same set. If they don't share the same parent then they belong to different sets.

To accomplish this:
- A single hashset {node : node's_parent}
- Initially we set every node's parent to itself as every node is in the set by itself
- We can merge two sets by setting one node's parent to the other node's parent
- We can find what the set id node is by recursively moving up the chain of parents to find the parent which points back to itself
- That accomplished a union operation in O(1) and a find operation that has best case O(1), average case O(log(n)) and a worst case O(n) for a maximum depth tree.

    class UnionFind:
        def __init__(self):
            self.id = {}  # Hashset to track the parents of nodes
        def find(self, x):
            y = self.id.get(x, x) # if the parent of x doesn't exist, return the node itself
            if y != x:
                y = self.find(y) # Recursively find the parent
            return y

        def union(self, x, y):
            self.id[self.find(x)] = self.find(y) # set the value to set id node of node y
## Trie
Problem: Given a set of strings, how many strings have a given prefix ?
More complexity: What if we wanted to support an indefinit amount of prefix queries and optential new string insertions into our set?

To achieve this we use a Trie data structure. This data structure is constructed from strings and generates a tree based on the characters of the string. We start from the leftmost charactera nd connect each of the new characters as a node of the tree

At this point we can modify the nodes to carry any information we deem necessary. In one case we can store a frequency variable at the node to count the number of strings with a certain prefix

## Segment Tree
Segment trees allow su to quickly perform range queries as well as range updates. Supopose we had an array and we wanted to know the sum of a particular range of numbersa s well as update the array when necessary. Normally, if we were to use just an array, updating would take O(1) time but a sum query could take up to O(n). Segment trees make both operations a O(log(n)) operation.

### Array to tree:
Segment trees work by breaking down the array into a binary tree where each node represents a segment of the array. Each node in the binary tree is created by taking the existing segment, cutting it in half and distributing it to the children nodes.


