import time
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)

        if 1 not in nums:
            return 1

        for i,v in enumerate(nums):
            if v <= 0 or v > N:
                nums[i] = 1

        for v in nums:
            if nums[abs(v)-1] > 0:
                nums[abs(v)-1] = -nums[abs(v)-1]

        for i,v in enumerate(nums):
            if v > 0:
                return i+1

        if nums[0] > 0:
            return N
        return N + 1
        

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.firstMissingPositive(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test(2, [3,4,-1,1])
test(3, [1,2])
test(3, [1,2,0])
test(1, [7,8,9,11,12])
test(5, [1,1,2,3,4])
