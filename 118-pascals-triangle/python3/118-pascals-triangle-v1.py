import time
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res: List[List[int]] = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1, 1])
            else:
                res.append([1])
                for j in range(1, i):
                    res[-1].append(res[i-1][j-1] + res[i-1][j])
                res[-1].append(1)
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
