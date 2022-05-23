'''
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
'''

def top_down_solution_3_state_variables():
    n = 4
    if n <= 1:
        return n
    if n == 2:
        return 1
    prev_1 = 0
    prev_2 = 1
    prev_3 = 1
    new = None
    for i in range(3,n+1):
        new = prev_1 + prev_2 + prev_3
        prev_1 = prev_2
        prev_2 = prev_3
        prev_3 = new
    return new

def top_down_solution_with_array():
    if n <= 1:
        return n
    if n == 2:
        return 1
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1 
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[-1] 


if __name__ == '__main__':
    main()
