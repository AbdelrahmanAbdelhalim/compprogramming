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

Example: [climbing_stairs.py](https://github.com/AbdelrahmanAbdelhalim/compprogramming/blob/master/dynamic_programming/climbing_stairs.py)
---
# Fifth Card (Multidimensional DP):

The dimension so f a DP alogirthm refer to the number of state variables used to define each state. Typically the more dimensions a DP has the more difficult it is to solve.

## Typical things to look for in DP problems that require a state variable:
* An index along some input. Which was the sole state variable we considered up to this point. And it has always represented the soltuion about to that index in the input array. So say input: nums = [1,2,3,4] then dp(2) is the solution for the problem up
* A second index along some input. Sometimes you need to index state variables. In some cases the variables represent the answer to the original problem if you considered the input starting at index i and ending at index j. Using the same example above dp(1,3) would represent the answer for [1,2,3]
* Numerical constraints given such as, you are only allowed to rob 3 houses
* Variables that describe statuses in a given state such as: true if holding a key and false if not
* tuple or bitmask to indicate things visited and used. Mutable data structures can not be used since they are not hashable and therefore ints and strings are to be used
---
# Sixth Card (Top down to Bottom up)

## Steps to converting from top down to bottom up:
* Start with a complete top down solution
* Initialize an array dp that is sized according to your state variables. For example: if the input to the problem was an array nums and an integer k that represents the maximum number ofa ctions allowed. The array would be a 2D with one dimension with length nums and the other with length k. The values should be initialized as some efault value opposite of what the problem is asking for. If the problem is asking for a maximum of something, set the values to negative infinity. If it is asking for the minimum of something, set the values to infinity.
* Set the base cases just as you have set them up for the Top down solution
* Write for-loops to ieterate over your state variables. If you have multiple state variables you will need nested for loops. They should start iterating from the base cases
* Each iteration of the inner most loop represents a given state and is equivalent to a function call to the same state in top-down. Copy the logic from the function into the for loop basically
* And that is about it!
---
# Seventh card (Example problem)
In this article we discuss maximum score from performing multiplication operations.

Problem Statemtent:

    You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

    You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

    Choose one integer x from either the start or the end of the array nums.
    Add multipliers[i] * x to your score.
    Remove x from the array nums.

    Return the maximum score after performing m operations.

We need to know 3 things for each operation:
* How many operations we have performed so far ?
* Index of the rightmost element left in nums
* Index of the leftmost element left in nums
Even though it might feel like we need those 3 variables but we can deduce one from the other two. If we know how many elements we picked from the left and we know how many operations we have performed then we can find right where right = n - 1 - (i - left). So we can keep track of i and left and calculate right on the fly

Now we have the state variables, what should the function return ? The problem is asking for the max score for some number of operations. So let us have dp(i,left) be the maximum possible score if we have done i total operations and used left numbers from the left side

Recurrent Relation:
dp(i,left) = max(mult[i]xnums[left] + dp(i+1,left+1), mult[i]xnums[right] + dp(i+1,left))

Base cases:
We are only allowed to perform m operations. That means when i equals m that we have no operations left and therefore should return 0

Practical implementation:
Note: @lru_cache can be useful to memoize the function. (Depending on interviewer obvs)

Bottom up solution:
The extra difficulty of bottom up can be seen in this problem. We use a lot of the same logic from the top down solution. We caclulate right the same way, we use the same recurrence relation etc.. But we need to iterate backwards starting from m (because the base case happens when i equals to m). We also need to initialize dp with one extra row so that we don't go out of bounds for the first iteration of the outer loop
---
# Eigth Card (Iteration in the recurrence relation)
For all the problems so far the recurrence relation is a static equation. For exampke in the min cost climbing stairs problem we could only take 1 or 2 steps at a time. But what if we could take up to k steps at a time? The recurrence relation then becomes dynamic - it would be: dp(i) = min(dp(j) + cost[j]) for all (i-k) <= j < i
We would need iteration in our recurrence relation.
---
# Card 9 (Example: Minimum difficulty of a job schedule)
Probelm statement:

    You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

    You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

    You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

## State variables
* i where i is the index of the first job that will be done on the current day
* day where day indicates the day we are currently at
Let's have a function dp(i,day) that returns the minimum difficulty of a mob schedule which starts on i^th job and day. To solve the original problem, we will just return dp(0,1).

## Recurrence relation
    At weach state, we are on day 'day' and we need to do jjob i. The problem states that we have to do at least 1 job per day, that means we must leave at least d - day jobs (where d is the number of days from the problem statement and days is the current day) so that all future days have at least 1 job to do on that day. If n is the total number of jobs, that means that for any given state (i, day), we are allowed to do the jobs from index i up to but not including index n - (d - day)

    We should try all options for a given day - try doing only one job, then two jobs, etc. Until we can't do any more jobs. The best opeiton is the one that results in the easiest job schedule.

    The difficulty of a given day is the most difficult job that we did on that day. Since the jobs have to be done in order, if we are trying all the jobs we are allowed to do on that day (iterating through them), then we can use a variable hardest to keep track of the difficulty of the hardest job done today. I we choose to do jobs up to the jth job (inclusive) where i <= j < n - (d-day), then on the next day, we start with the (j+1)th job. Therefore our total difficulty is hardest + dp(j+1, day+1).

    Finally giving us the scary recurrence relation: dp(i,day) = min(hardest + dp(j+1,day+1)) for all i <= j < n - (d-day) where hardest = max(jobDifficulty[k]) for all i <=k <= j

## Base Cases
    We need to finish all jobs in d days. Therefore if it is the last day (day == d), we need to finish up all the remaining jobs on this day, and the total difficulty will just be the largest number in jobDifficulty on or after index i.
    if day == d then return the maximum job difficulty between job i and the end of the array (inclusivei)
    Additionaly we can also pre-compute an array hardesJobRemaining[i] representing the difficulty of the hardest job on or after day i, so that the base cases are handled in constant time.
    Another base case is if there are more days than jobs in which case we can't possibly schedule the jobs. Therefore returning -1

