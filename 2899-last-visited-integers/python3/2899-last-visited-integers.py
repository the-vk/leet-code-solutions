class Solution:
  def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
    seen = []
    ans = []
    ks = 0
    for v in nums:
      if v > 0:
        seen.insert(0, v)
        ks = 0
      else:
        ks += 1
        if ks <= len(seen):
          ans.append(seen[ks-1])
        else:
          ans.append(-1)
    return ans