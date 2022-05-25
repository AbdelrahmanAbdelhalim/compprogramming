'''Problem Statement:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''
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

    1.Divide and Conquer:
      The idea is to compare the first two letters of the strings. If they match then the divide the problem and solveit for s[1:] and t[1:]
      If they don't match then solve for s[0:] and t[1:]
      Define the base cases. And do it recursively.
      - Time complexity: O(|T|)
        At each invocation we would conuse one character from the target string and maybe one
        character from the source string
        In the worst case we would have to scan all of T and therefore the complexity is O(|T|)
      - Space complexity: O(|T|)
        Recursion incures a higher memory consumption in the function call stack. Tail recursion
        can improve complexity but python and java don't support them
        (@TODO: Research tail recursion)
    
    2.Two pointers:
      Use two pointers one for target and one for source:
        1.If you find a match move both pointers one step
        2.If no match then move the pointer for target string one step
      Recursion terminates when one of the pointers exceeds either string
      - Time Complexity: O(|T|)
        Same as previous approach
      - Space Complexity: O(1)
        Replacing recursino with iteration results in a constant memory consumption
    
    3.Greedy Match with Character indicies Hashmap (IMPORTANT)
      This tackles the question of getting multiple source strings and a single target string
      Previous algorithms would do the strings individually resulting in O(|T|) time per string
      Since we would have to scan the target string repetedly.
      We can think about the scanning as a lookup operation
      We can build a hashmap of the target strings with the keys as each unique character and the
      value as the indices of its appearance (We should precompute it once)
    
    4.DP (Great example when DP sucks compared to other algorithms)
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



