'''
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        '''Performance on leetcode
        Runtime: 1494 ms, faster than 5.38% of Python3 online submissions for Decode Ways.
        Memory Usage: 14 MB, less than 46.07% of Python3 online submissions for Decode Ways.
        '''
        memo = {}
        def traverse_tree(remaining_string):
            nonlocal memo
            if len(remaining_string) <= 0:
                return 1
            elif len(remaining_string) == 1 and int(remaining_string) > 0:
                return 1
            if int(remaining_string[0]) <=0:
                return 0
            if memo.get(remaining_string):
                return memo[remaining_string]
            first_two_numbers = remaining_string[0:2]
            if int(first_two_numbers) <= 26:
                first = traverse_tree(remaining_string[1:])
                second = traverse_tree(remaining_string[2:])
                memo[remaining_string] = first + second
                return first + second
            else:
                
                return traverse_tree(remaining_string[1:])
        ans = traverse_tree(s)
        return ans
