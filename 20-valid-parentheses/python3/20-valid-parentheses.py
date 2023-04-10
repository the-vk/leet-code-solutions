class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for b in s:
            if b in brackets:
                stack.append(brackets[b])
            elif len(stack) == 0 or b != stack.pop():
                return False
        return len(stack) == 0
