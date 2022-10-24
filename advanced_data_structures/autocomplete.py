"""Problem Statement
Given a dictionary, containing a list of words, and a list of queries, which consists of a list of prefixes, compute the result of each query. Each query is simply a string denoting a prefix. For each query, return the number of words in the dictionary that contains that prefix.

Only lower-case English letters will be used.
Constraints

1 <= words.length <= 100001

1 <= words[i].length <= 10
Examples
Example 1:
Input: words = ["forgot", "for", "algomonster", "while"], prefixes = ["fo", "forg", "algo"]
Output: [2, 1, 1]
Explanation:

"forgot" and "for" have the prefix "fo". Only "forgot" has "forg", and only "algomonster" has the prefix "algo".
"""

from typing import List

class trie():
    def __init__(self, x):
        self.val = x
        self.children = {}
        self.count = 0

    def insert(self, x, idx):
        if idx == len(x):
            return
        new_node = self.children.setdefault(x[idx], trie(x[idx]))
        new_node.count += 1
        new_node.insert(x, idx + 1)

    def query(self, prefix, idx):
        if len(prefix) == idx:
            return self.count

        nxt = self.children.get(prefix[idx])
        if nxt is None:
            return 0
        return nxt.query(prefix, idx + 1)

def prefix_count(words: List[str], prefixes: List[str]) -> List[int]:
    dic = trie("$")
    ans = []
    for word in words:
        dic.insert(word, 0)

    for prefix in prefixes:
        ans.append(dic.query(prefix, 0))
    return ans

