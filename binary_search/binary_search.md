# Binary Search
Binary search is an efficient way to search arrays. We start by looking at the middle of the array. If the element at the middle of the array matches the target the we return. However, if the value is smaller than the target then we move the right pointer to mid - 1 since we know we need to look for the result in that section of the array. If the element in the middle is bigger then we move l to mid + 1 for similar reasons. if l > r at that point we know that the element is not in the array

## Calculating mid
If the number of elements is even, there are two elements in themiddle, we usually pick the first one equivalent to the integer division of (left + right) / 2. In most programming languages, we calculate mid with left + floor((right-left)/2) to avoid potential integer overflow. However, in python we do not need to worry about integer overflow.

## Deducing binary search.
To deduce the algorithm there are three main questions to answer:
    - When to terminate the loop: You need to remember to use <= in the while loop as not to miss on the value of l = r (made that mistake)
    - How to update left and right: easy
    - Discarding the current element. In vanilla binary search we would discard the current element but in some situation we might not want to do that

## When to use binary search
Binary search works whenever we want to make a binary decision that shrinks the search range.
