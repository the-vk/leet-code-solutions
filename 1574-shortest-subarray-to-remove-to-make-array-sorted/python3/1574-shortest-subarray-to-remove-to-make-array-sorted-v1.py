import time
from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        left, right = 0, N-1
        while left < right and arr[left] <= arr[left+1]:
            left += 1
        if left == right:
            return 0
        min_sub = 0
        while right > 0 and arr[right-1] <= arr[right]:
            right -= 1
        min_sub = min(N - left - 1, right)

        for i in range(left + 1):
            if arr[i] <= arr[right]:
                min_sub = min(min_sub, right - i - 1)
            elif right < N-1:
                right += 1
            else:
                break
        return min_sub

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.findLengthOfShortestSubarray(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test(3, [1,2,3,10,4,2,3,5])
test(4, [5,4,3,2,1])
test(0, [1,2,3])
test(0, [1])