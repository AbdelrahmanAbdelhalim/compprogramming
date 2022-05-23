'''Problem Statement:
    Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    '''Solution Result on leetcode:
    Runtime: 44 ms, faster than 44.61% of Python3 online submissions for Pascal's Triangle II.
    Memory Usage: 13.9 MB, less than 16.93% of Python3 online submissions for Pascal's Triangle II.
    A better solution can only use one array instead of keeping old array in its own spot
    '''
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        last_row = [1,1]
        for i in range(2,rowIndex + 1):
            new_row = [0 for l in range(i+1)]
            new_row[0], new_row[-1] = 1,1
            for j in range(1,len(last_row)):
                new_row[j] = last_row[j] + last_row[j-1]
            last_row = new_row
        return last_row
