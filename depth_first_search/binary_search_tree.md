# What is a BST
A rooted binary tree with the value of each internal node greater than all the values in the respective
node's left subtree and less the ones in its right subtree.

An empty root is a BST since it satisfies the BST definition. The values can be of any type as long as they are comparable with each other.

## Searching
The purpose of the BST is to search. In particular, you can search for the existence of an element in the same time you would
if you were doing a binary search.
Complexity of the search is o(h) where h is the height of the tree. In the best case scenario the height of the tree is
proportional to the log of the size of the tree.

## Insertion
Advanatage of a BST over a sorted list is that insertion does not require items in the list to move an index. Instead,
we perform a search for that item in the BST. However, if we find an empty tree instead we replace that empty tree with
a new node containing the inserted value in the BST.
The time complexity is the same as searching: O(h)

## Deletion (Optional)
Deletion does not show up often in coding interview. However, for completeness purposes: deleting an item in a BST is done by
finding the node first.
    - If the right subtree of the node is empty, bring its left subtree to its current position
    - Otherwise, delete the leftmost node of the right subtree and put it in in its current position
Time complexity: Proportional to the height of the tree as before O(h)

## Improvements (Optional)
Ideally the time complexity of each operation is O(log(n)). However, if we build a binary tree from a sorted list we will end
up with a linked list and all operations will become O(n).

Here we introduce balanced binary trees. A balanced binary tree whose subtrees are also balanced and have height difference of
at most 1. One of the self-balancing trees is the AVL trees. It uses 'Tree Rotation' at ceratin points of insertion. If on insertion one of the nodes becomes unbalanced then one of the subtrees must have two more height than others. Depending on which side is unbalanced, the balancing act is different.

## Applications
BST is often used to look up the existence of certain objects. Compared to sorted arrays, the insertion has way lower time
complexity. So it is good for dynamic insertion of items. If we don't need to dynamically insert new items, then we can simply sort the collection first and use binary search to look up.

Most modern languages offer hash tables which is another way of looking up existince of an object. Most implementations are
dynamically sized, which can cause lookup and insertion of items to approach O(1). Therefore, usually hash tables are preferred to BST. Nevertheless, there are some advantages to using a BST over a hash table.
    -  Hash tables are unsorted while BSTs are.
    - It is easy to lookup the first element in the BST that is greater/smaller than a look up value than a hash table
    - It is easy to find the k-th largest/smallest element.
    - Dynamic hash tables usually have a lot of unused memory
    - Dynamic hash tables usually have a lot of unused memory to support O(1) lookup while BSTs use all the space they require

