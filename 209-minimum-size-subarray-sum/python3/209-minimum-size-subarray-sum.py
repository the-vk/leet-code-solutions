class Solution:
  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    ans = len(nums) + 1
    l = r = 0
    s = nums[l]
    while r < len(nums):
      if s >= target:
        ans = min(ans, r-l+1)
        s -= nums[l]
        l += 1
      else:
        r += 1
        if r < len(nums):
          s += nums[r]
    if ans == len(nums) + 1:
      return 0
    return ans