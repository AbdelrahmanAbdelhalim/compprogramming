"""Problem Statement
Given 2 strings determine the minimum cost required to delete characters from either string to make them equal. We also assign a particular cost to each character so that in order to remove one instance of that character from either string it will inccur that cost. Only lower-case English letters will be used. The answer is guarenteed to fit in a 32-bit integer.
Input

    costs: An array of size 26 that contains the cost for each character in the order of a-z
    s1: First string
    s2: Second string

Output

Minimum cost to make the strings equal
"""


# Bottom Up solution
from typing import List
import math


def plist(foo):
    for fo in foo:
        print(fo)


def delete_string(costs: List[int], s1: str, s2: str) -> int:
    dp = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        dp[i][0] = dp[i - 1][0] + costs[ord(s1[i - 1]) - ord('a')]

    for j in range(1, len(s2) + 1):
        dp[0][j] = dp[0][j - 1] + costs[ord(s2[j - 1]) - ord('a')]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1] + costs[ord(s2[j - 1]) - 97], dp[i - 1][j] + costs[ord(s1[i - 1]) - 97])
    return dp[-1][-1]

