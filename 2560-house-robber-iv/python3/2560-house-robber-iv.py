class Solution:
  def minCapability(self, nums: List[int], k: int) -> int:
    l, r = min(nums), max(nums)
    while l < r:
      m = (l + r) // 2
      took = 0
      robbed = 0
      for v in nums:
        if robbed:
          robbed = 0
          continue
        if v <= m:
          took += 1
          robbed = 1
      if took >= k:
        r = m
      else:
        l = m + 1
    return l
