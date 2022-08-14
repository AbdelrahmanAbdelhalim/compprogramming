'''This was easy because you drew the tree
A nice idea is thinking of the output as the nodes you are going to
visit as well
'''
def is_palindrome(word: str):
    l = 0
    r = len(word) - 1
    while l <= r:
        if word[l] != word[r]:
            return False
        else:
            l += 1
            r -= 1
    return True

def partition(s: str) -> List[List[str]]:
    def traverse(path_so_far, remainder, ans):
        if len(remainder) <= 0:
            ans.append(path_so_far.copy())
            return
        for i in range(1, len(remainder) + 1):
            current_partition = remainder[:i]
            if is_palindrome(current_partition):
                path_so_far.append(remainder[0:i])
                traverse(path_so_far, remainder[i:], ans)
                path_so_far.pop()
    ans = []
    path_so_far = []
    traverse([], s, ans)
    return ans

