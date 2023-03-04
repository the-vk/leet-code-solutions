class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
      result = 0
      left = right = out = -1
      for i, v in enumerate(nums):
        if not minK <= v <= maxK:
          out = i
        if v == minK:
          left = i
        if v == maxK:
          right = i
        result += max(0, min(left, right) - out)
      return result