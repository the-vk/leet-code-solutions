class Solution:
  def maxFrequencyElements(self, nums: List[int]) -> int:
    t = {}
    for x in nums:
      if not x in t:
        t[x] = 0
      t[x] += 1
    m = max(t.values())
    ans = 0
    for x in t.values():
      if x == m:
        ans += x
    return ans