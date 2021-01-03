import time
from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {}
        brackets['('] = ')'
        brackets['['] = ']'
        brackets['{'] = '}'
        stack = []
        for b in s:
            if b in brackets:
                stack.append(brackets[b])
            elif len(stack) == 0 or b != stack.pop():
                return False
        return len(stack) == 0
            
                

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.isValid(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test(True, "{[]}")
