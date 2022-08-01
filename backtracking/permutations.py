'''Problem Statement
Given a string of unique letters, find all of its distinct permutations.
Input

    letters: a string of unique letters

Output

all of its distinct permutations
'''

# My solution
from typing import List

def permutations(letters: str) -> List[str]:
    ans = []
    def traverse_search_tree(current_list, remaining_letters):
        nonlocal ans
        if not remaining_letters:
            ans.append(''.join(current_list))
            return
        for letter in remaining_letters:
            new_state = current_list.copy()
            new_state.append(letter)
            new_remaining_letters = remaining_letters.copy()
            new_remaining_letters.remove(letter)
            traverse_search_tree(new_state, new_remaining_letters)
    traverse_search_tree([], list(letters))
    return ans

if __name__ == '__main__':
    letters = 'abc'
    res = permutations(letters)
    for line in res:
        print(line)

'''Improvements on the solution
Instead of constructing new lists to track the states which pours into space complexity
we can instead use a used[] array to track the letters that have been used so far.
And instead of constructing a new list to track the current string, we can instead use a single
list and pop it after the recursive call and set the used letter to False
'''
