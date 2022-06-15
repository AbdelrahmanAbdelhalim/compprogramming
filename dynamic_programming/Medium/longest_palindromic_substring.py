class Solution:
    '''Performance on leetcode:
        - Runtime: 878 ms, faster than 86.11% of Python3 online submissions.
        - Memory Usage: 13.9 MB, less than 90.66% of Python3 online submissions.

        Thinking steps:
        1. Think of the bruteforce solution:
            - Get all the substrings in the array and check if they are a palindrome and check their length
              This results in complexity: O(N^3) -> N^2 substrings and O(N) to check if it is a palindrome
        2. Think of how to save time with dp
            - We can save time when validating palindromes by storing the results in a 2d array where:
              dp[i][j] is the length of the longest palindrome for the string that starts at i and ends at j
        3. Think of a creative bottom up soution:
            - If we expand around the center we can save a huge amount of memory since we will only need
              to keep track of the length of the inner palindromes for the center we are computing. We don't
              need to keep the other lenghts in memory in that case scenario.
    '''
    def longestPalindrome(self, s: str) -> str:
        max_left = 0
        max_right = 0
        if not s or len(s) < 1:
            return ''
        
        for i in range(len(s)):
            center_1 = self.expand(s,i,i+1)
            center_2 = self.expand(s,i,i)
            mx_ln = max(center_1, center_2)
            if mx_ln > (max_right - max_left + 1):
                max_left = int(i - (mx_ln - 2) / 2)
                max_right = int(i + mx_ln / 2)
        return s[max_left: max_right+1]
        
        
    def expand(self, s, l ,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
