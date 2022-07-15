# Stacks
First in last out data structure similar to a deck of cards or a stack of papers
Supports three operations:
    - Insert or Push: Putting an item on top of the stack
    - Peek: Look at the top item of the stack
    - Remove or Pop: Remove the top item fom the stack

## Implementation:
A basic implementation of the stack is a statically sized array and a pointer pointing to the top of the stack. When inserting an item we set the value of the pointer to that item and bump the pointer by 1. When removing a pointer we decrement the pointer at the top of the stack. There is no need to reset the item in the pointer because it is not accessible by the stack however it might still be good to do that for languages with garbage collectors to prevent memory leaks.

Popping an empty stack can cause an underflow error, which can be prevented by checking if the stack has any items before performing a pop. Overflow errors can also happen if you try to add items after you have reached the size limit of the array. For modern programming languages there is usually a dynamically sized array data structures. They can be used as a stack and since space is dynamically allocated to a list we don't have to worry about overflowing. In Python we can use the default list as a stack and in java we can use ArrayList. Java has built in Stack class designed for synchronization (However, Slower than an ArrayList)
