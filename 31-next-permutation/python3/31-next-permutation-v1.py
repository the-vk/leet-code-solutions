import time
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot = i-1
                break
        if pivot >= 0:
            for j in range(len(nums)-1, pivot, -1):
                if nums[pivot] < nums[j]:
                    self.swap(nums, pivot, j)
                    break
        self.reverse(nums, pivot + 1)
        return nums

    def swap(self, nums: List[int], l: int, r: int):
        t: int = nums[l]
        nums[l] = nums[r]
        nums[r] = t

    def reverse(self, nums: List[int], i: int):
        l, r = i, len(nums) - 1
        while l < r:
            self.swap(nums, l, r)
            l+= 1
            r -= 1

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.nextPermutation(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
            # raise ValueError("solution is invalid!")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test([2,3,3,1,3], [2,3,1,3,3])
test([1,3,2], [1,2,3])
test([1,2,3], [3,2,1])
test([1,5,1], [1,1,5])
test([1], [1])

print("solution is correct!")
