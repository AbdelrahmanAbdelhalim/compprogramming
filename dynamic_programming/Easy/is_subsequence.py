'''Problem Statement:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''First solution (that I came up with)
        Solution result on leetcode:
            - Runtime: 51 ms, faster than 37.20% of Python3 online submissions.
            - Memory Usage: 14 MB, less than 19.10% of Python3 online submissions.
        '''
        progress_pointer = 0
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        
        for letter in t:
            if progress_pointer >= len(s):
                return progress_pointer == len(s)
            if letter == s[progress_pointer]:
                progress_pointer += 1
        return progress_pointer == len(s)

'''This problem has multiple solutions:
    - Divide and Conquer
    - Two-Pointers
    - Greddy Match with Character indices Hashmap
    - DYnamic Programming
    There is an interesting question asked at the end of the problem statement:
    What if we have multiple inputs at a time for the same t. What can we do to further
    optimize the solution?
    Below is a breakdown of the solution since this problem is a rather common one in computer
    science in general and will be met at all levels of difficulty.

'''

