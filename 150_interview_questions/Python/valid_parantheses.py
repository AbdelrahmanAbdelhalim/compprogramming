"""Problem Statement
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.


"""

class Solution:
    def isValid(self, s: str) -> bool:
        expect = []
        for i in range(len(s)):
            if s[i] == "(":
                expect.append(")")

            elif s[i] == "{":
                expect.append("}")

            elif s[i] == "[":
                expect.append("]")

            else:
                if len(expect) > 0:
                    if expect[-1] == s[i]:
                        expect.pop()
                    else:
                        return False
                else:
                    return False

        return True if len(expect) == 0 else False

