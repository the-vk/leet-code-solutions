import time
from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            for j in range(len(res)-1, -1, -1):
                res.append(res[j] + 2**i)
        return res
        

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.grayCode(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test([0,1,3,2], 2)
test([0], 0)