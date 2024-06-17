class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    seen = set()
    for x in nums:
      seen.add(x)
    for x in range(len(nums) + 1):
      if x not in seen:
        return x