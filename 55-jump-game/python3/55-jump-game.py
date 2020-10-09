import time
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        t = len(nums) - 1
        for i in range(t, -1, -1):
            if (t - (i + nums[i])) <= 0:
                t = i
        return t == 0

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.canJump(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
            # raise ValueError("solution is invaid!")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test(True, [2,3,1,1,4])
test(False, [3,2,1,0,4])
test(False, [0, 1])

print("solution is correct!")
