def solution(n):
    non_memo = dp(n) ## Runs in O(2^N)
    memo = dp_memo(n) ## Runs in O(N)

## Top Down Solution without memoization (basic recursion)
def dp(i):
    if i <= 2:
        reutrn i
    return dp(i-1) + dp(i-2)

## Top Down Solution with memoization
memo = {}
def dp_memo(i):
    if i <= 2:
        return i
    if i not in memo:
        memo[i] = dp(i-1) + dp(i-2)
    else:
        return memo[i]
    
## Bottom Up Solution
def dp_bottom_up(n):
    if n == 1:
        return 1
    dp = [0] * (n+1) ## Array to store the solutions at every stage

    ## Base cases
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

