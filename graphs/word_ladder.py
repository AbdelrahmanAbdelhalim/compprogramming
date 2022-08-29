'''Problem Statement
Word Ladder is "a puzzle begins with two words, and to solve the puzzle one must find a chain of other words to link the two, in which two adjacent words (that is, words in successive steps) differ by one letter."

For example: COLD → CORD → CARD → WARD → WARM

Given a start word, an end word, and a list of dictionary words, determine the minimum number of steps to go from the start word to the end word using only words from the dictionary.

Input:

start = "COLD"

end = "WARM"

word_list = ["COLD", "GOLD", "CORD", "SOLD", "CARD", "WARD", "WARM", "TARD"]

Output:

4
'''

'''Important note
We can save a lot of memory by building the graph as we go instead of building it all at once at the beginning like in this solution. The conversion is a rather easy step.
'''
from collections import deque

from typing import List

def word_ladder(begin: str, end: str, word_list: List[str]) -> int:
    def build_adjacency_list(wordlist):
        adjacency_list = {}
        for word in wordlist:
            res = []
            for secondword in wordlist:
                diff = 0
                for i in range(len(word)):
                    if word[i] == secondword[i]:
                        continue
                    else:
                        diff += 1
                if diff == 1:
                    res.append(secondword)
            adjacency_list[word] = res
        return adjacency_list

    def get_neighbors(word, adjacency_list):
        if adjacency_list.get(word):
            return adjacency_list[word]
        else:
            return {}

    def traverse(begin, end, graph):
        stack = deque({begin})
        current_level = -1
        visited = set()
        while len(stack) > 0:
            current_level += 1
            for _ in range(len(stack)):
                node = stack.popleft()
                if node in visited:
                    continue
                visited.add(node)
                if node == end:
                    return current_level
                neighbors = get_neighbors(node, graph)
                for neighbor in neighbors:
                    stack.append(neighbor)
        return -1
    
    adjacency_list = build_adjacency_list(word_list)
    return traverse(begin, end, adjacency_list)
