# First Card (What is DP):
---
* DP is a paradigm that systematically explores all possible solutions to a problem</li>
* Problems that have the following characteristics can be solved by DP:</li>
    * Can be broken down into 'overlapping subproblems'. Smaller versions of the original problem can be used multiple times
    * The problem has an optimal structure. An optimal solution can be formed from optimal solutions to the overlapping subproblems of the original problem
Don't confuse divide and conquer with DP. Divide and Conquer divides a problem into subproblems but it doesn't have overlapping subproblems
---
# Second Card (Top-down and Bottom-up):
* Bottom up:
    Bottom up is implemented with iteration and it starts at the base cases.
* Top Down:
    Implemented with recursion and made efficient with 'memoization'. Start at the big case and compute down to the base cases recursively

* Memoization:
    Memoization is saving the result of a function call usually in a hashmap or an array so when we call that function again the result is readily available and we don't waste time recomputing it again

* Advantages and disadvantages of Top down and Bottom up approaches:
    * bottom up usually has better runtime, usually faster. As iteration does not have the overhead that recursion does
    * top down usually is much easier to write. Because with recursion the ordering of the subproblems does not matter. Whereas with tabulation we need to go through a logical ordering of solving subproblems
---
# Third Card (When to use DP):
* Characteristics of a DP problem:
    * Usually asks you to find the maximum or a minimum of something.
    * Future decisions depend on earlier decisions.

The second characteristic is not well defined. The key around this is to try to come up with counter examples to why you should use a greedy algorithm, if you have one case which points to not using it then it is a good indication to use DP.
These characteristics are only guidelines.
---
# Fourth Card (Framework for DP):
* Defining State:
     A state is a set of variables that can sufficiently describe a scenario. Relevant variables are only included in the statue

* THE FRAMEWORK:
    * A function or data strucuture that will compute/contain the answer to the problem at every given state
    * A recurrent relation to transition between states (Sort of like proof by induction)
    * Base cases.

Example: [a link](https://github.com/AbdelrahmanAbdelhalim/compprogramming/blob/master/dynamic_programming/climbing_stairs.py)

