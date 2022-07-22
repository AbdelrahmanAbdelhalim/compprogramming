# DFS on trees

## Think like a node
Key to solving tree problems using DFS is to think from the perspective of a node instead of looking at the
whole tree. Decide how the current node should be proceeded, then recurse on children and let recursion take
care of the rest.

## Defining the recursive function

Two things we need to decide
    - Return value: what we want to return after visiting a node
    - Identify states: what states do we need to maintain to compute the return value for the current node

## Using return value vs global variable
We can either return values as we traverse the trees or use a global variable to keep track if our target.
It is down to personal preference which noe to use. Sometimes it is easier to use global variables but it
can be argued that global variables are bad and should not be used. 'End of the day Personal Preference'
