class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
      return max(ceil(a / (i+1)) for i,a in enumerate(accumulate(nums)))