def letter_combinations_of_phone_number(digits: str) -> List[str]:
    KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
    }
    def traverse_tree(digits, current_string, depth, ans):       
        if depth >= len(digits):
            foo = ''.join(current_string)
            ans.append(foo)
            return
        letters = KEYBOARD[digits[depth]]
        for letter in letters:
            current_string.append(letter)
            depth += 1
            traverse_tree(digits, current_string, depth, ans)
            current_string.pop()
            depth -= 1
    ans = []
    current_string = []
    depth = 0
    traverse_tree(digits, current_string, depth, ans)
    return ans

