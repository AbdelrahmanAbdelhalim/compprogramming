'''Problem Statement
You commissioned a locksmith to craft a special combination lock for you, because you are a lich and you want to hide your phylactery in somewhere secure. It looks like a regular 4-digit combination lock, with each digit can be one of the digits from 0~9. Each digit can be turned forwards by 1 and backwards by 1, and the first and the last digit is connected (9 goes to 0 when moving forward, and 0 goes to 9 when moving backward). The lock starts at 0000.

However, because you don't want people to find your phylactery, you have trapped certain combinations of this combination lock. If someone were to set the combination to a trapped combination, bad things happen to them, which this question would not elaborate upon.

You know the combination, and you know the trapped combinations. You wonder if the lock can be opened without triggering the traps, and if so, how many digit changes must be made to the lock to unlock it.
Input

    target_combo: a string representing the four digit combination to open the lock.
    trapped_combos: a list of strings representing the trapped combinations.

Output

An integer representing the number of steps it takes to open the lock, or -1 if you can't open it without triggering the trap.
'''

'''This solution times out on one of the test cases, I still need to figure out the reason
'''
from typing import List
from collections import deque

def num_steps(target_combo: str, trapped_combos: List[str]) -> int:
    def get_neighbors(combination, trapped_combos, visited):
        new_combos = []
        for i in range(len(combination)):
            for j in [1,-1]:
                new_combo = ''
                new_combo += combination[:i]
                new_bit = int(combination[i]) + j
                if new_bit < 0:
                    new_bit = 10 + new_bit
                if new_bit > 9:
                    new_bit = new_bit - 10
                new_combo += str(new_bit)
                new_combo += combination[i+1:]
                if new_combo not in trapped_combos and new_combo not in visited:
                    new_combos.append(new_combo)
        return new_combos
    
    def traverse(combination, trapped_combos):
        stack = deque({"0000"})
        trapped_combos = set(trapped_combos)
        current_level = -1
        visited = set()
        while len(stack) > 0:
            current_level += 1
            for _ in range(len(stack)):
                node = stack.popleft()
                visited.add(node)
                if node == combination:
                    return current_level
                neighbors = get_neighbors(node, trapped_combos, visited)
                for neighbor in neighbors:
                    stack.append(neighbor)
        return -1

    return traverse(target_combo, trapped_combos)

if __name__ == '__main__':
    target_combo = input()
    trapped_combos = input().split()
    res = num_steps(target_combo, trapped_combos)
    print(res)

