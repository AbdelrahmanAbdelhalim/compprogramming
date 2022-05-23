'''Problem Statement:
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
    '''Solution result from leetcode:
    Runtime: 37 ms, faster than 68.28% of Python3 online submissions for Pascal's Triangle.
    Memory Usage: 13.8 MB, less than 97.71% of Python3 online submissions for Pascal's Triangle.
    '''
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        dp = [None for i in range(numRows)]
        dp[0] = [1]
        dp[1] = [1,1]
        for i in range(2,numRows):
            previous_row = dp[i-1]
            new_row = [0 for k in range(len(previous_row) + 1)]
            new_row[0], new_row[-1] = 1,1
            for j in range(1,len(dp[i-1])):
                new_row[j] = previous_row[j] + previous_row[j-1]
            dp[i] = new_row
        return dp
