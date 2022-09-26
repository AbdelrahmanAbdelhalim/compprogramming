# Priority Queues and Heaps

Priority queue is an abstract data type. A heap is the concrete data structure used to implement a priority queue

## Priority Queue
Data structure that consists of a collection of items and supports:
- insert: insert an item with a key
- delete_min/delete_max: remove the item with the smallest/largest key and returning it

## Kinds of heaps

- Min Heap
- Max Heap

trees that have two properties:
- almost complete: every level is filled except possibly the last level. The filled items in
the last level are left justified
- For any node, its key is greater than its parent's key

Nodes in the same level of a heap have no comparable properties

## Why heaps are useful

- Because heap is a complete tree. The height of the heap is guranteed to be O(log(n)). That makes operations that go from root to leaf guaranteed to be O(log(n))
- Because onlynodes in a root-to-leaf path are stored. (nodes in the same level are not stored). When we add/remove a node, we only have to fix the order in the vertical path the node is in. This makes inserting and deleting O(log(n)) too.
- Being complete also makes array a good choice to store a heap isnce datais continuous.


## Operations

### insertion
To insert a key into a heap:
- Place the new key at the first leaf
- if property #2 is violated, perform bubble up

    def bubble_up(node):
        while node.parent exist and node.parent.key > node.key:
        swap node and node.parent
        node = node.parent

Since the height of the tree is O(log(n)) the complexity of bubble up is O(log(n))

### delete_min
What this operation does
- delete a node with min key and return it
- reorganize the heap so the two properties still hold

To do that:
- Remove and return the root since the node with the minimum key is always at the root
- replace the root with the last node (The rightmost node at the bottom) of the heap
- If property #2 is violated perform bubble down

    def buble_down(node):
        while node is not a leaf:
            smallest_child = child of node with smallest key
            if smallest_child < node:
                swap node and smallest_child
                node = smallest_child
            else:
                break


## Implementing the heap
Stored in an array: For node i, its children are stored at 2i+1 and 2i+2. Parent is at floor((i-1)/2). So instead of node.left we do 2*i+1
