import time
from typing import List

class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        sum = 0
        count = 0
        for a in sorted(arr):
            sum += a
            if sum > 5000:
                break
            else:
                count += 1
        return count

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.maxNumberOfApples(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test(4, [100,200,150,1000])
test(5, [900,950,800,1000,700,800])
