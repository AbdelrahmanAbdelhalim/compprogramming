
"""
Determine whether a string is a palindrome, ignoring non-alphanumeric characters and case. Examples:

Find the length of the longest substring of a given string without repeating characters.

Input: abccabcabcc

Output: 3
"""
#aeefceyt
# cbaebabacd
# abc

from typing import List
def get_letter_count(check):
    letters = [0 for i in range(26)]
    for letter in check:
        letters[ord(letter) - ord('a')] += 1
    return letters
def find_all_anagrams(original: str, check: str) -> List[int]:
    if len(check) > len(original):
        return []
    letter_count = get_letter_count(check)
    window_tracker = [0 for i in range(26)]
    window_size = len(check)
    res = []
    for i in range(window_size):
        letter = original[i]
        window_tracker[ord(letter) - ord('a')] += 1
    if window_tracker == letter_count:
        res.append(0)
    r = len(check) - 1
    l = 0
    while r < len(original) - 1:
        window_tracker[ord(original[l]) - ord('a')] -= 1
        l += 1
        r += 1
        window_tracker[ord(original[r]) - ord('a')] += 1
        if window_tracker == letter_count:
            res.append(l)
    
    return res


