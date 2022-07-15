# Queues
A queue is a first in first out data structre (FIFO)

It supports three operations:
    - Insert or Push: Add an item to the queue
    - Peek: Look at the first item in the queue
    - Remove or Pop: Remove the first item in the queue
A deque is a double-ended queue. That means inserting and removing items from the queue can be done on both ends

#Implementation
We use an array with two pointer at the start and end. If we want to pop we increment the start pointer by 1 and if we want to queue we set the current pointer to that value and increment the pointer by 1.
For a dequeue we can ust the same logic but we allow the increment and decrement of both start and end pointers.
The issue with that implementaiton is when one of the queue poniters reaches the end of the array. However, if some elements have been removed from the other end, then when the queue overflows, there is still a lot of empty spaces.
An improvement can be done is to make the array loop. When a pointer tries to move past the array, it loops back around the array instead (Circular Buffer)

Most modern programming languages have build in deque data structures. Often using a dynamic array as the underlying data structure (Although they can use a double linked list like python's dequeue class)

To use a dequeue in python we use:
        from collections import deque
        queue = deque()
