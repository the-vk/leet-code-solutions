class Solution:
  def minIncrementForUnique(self, nums: List[int]) -> int:
    nums = sorted(nums)
    ans = 0
    for i in range(1, len(nums)):
      d = max(0, nums[i-1] - nums[i] + 1)
      ans += d
      nums[i] += d
    return ans