import time
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        for i in range(0, len(expression)):
            c = expression[i]
            if c in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[0:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if c == '+':
                            res.append(l + r)
                        elif c == '-':
                            res.append(l - r)
                        elif c == '*':
                            res.append(l * r)
        if len(res) == 0:
            res.append(int(expression))
        return res

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.generate(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test([
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
], 5)

test([
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1],
[1,5,10,10,5,1]
], 6)
