def decode_ways(digits: str) -> int:
    memo = {}
    def traverse_tree(remaining_string):
        if len(remaining_string) <= 0:
            return 1
        elif len(remaining_string) == 1:
            return 1
        first_two_numbers = remaining_string[0:2]
        if int(first_two_numbers) <= 26:
            first = traverse_tree(remaining_string[1:])
            second = traverse_tree(remaining_string[2:])
            nonlocal memo
            memo[remaining_string] = first + second
            return first + second
        else:
            return traverse_tree(remaining_string[1:])
    ans = traverse_tree(digits)
    return ans

