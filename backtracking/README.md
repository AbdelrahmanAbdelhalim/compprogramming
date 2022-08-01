# Backtracking
## Combintorial search problems
Combinatorial search problems involve finding groupings and assignments of objects that satisfy certain conditions. Finding all permutations/subsets, solving sudoko, and 8-queens are classical problems.

## Permutations
    - Permutation means arranging things in order.
    - Number of permutations is given by n!.

## Complexity
Complexity grows very rapidly with the size of the problem.
    - 3! = 6
    - 10! = 3M
    - 11! = 40M

## Combinatorial search == DFS
Interpret states as a tree where a tree with all possible states is called a state-space tree.

## Conquring combinatorial search problems
    - Identify the states
    - Draw that state-space tree
    - DFS/backtrackihng on the state-space tree
Most important step is to draw the tree: A small test case that is enough to reach at least one solution. Once we draw a mental map of the tree the problem becomes so much easier.
Searching and Backtracking is the first topic tackled in the book 'Aritificial Intelligence a modern approach'
Backtracking problems don't traverse an explicit tree. We essentialy generate the nodes as we traverse them in a way
