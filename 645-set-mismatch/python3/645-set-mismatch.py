from collections import Counter

class Solution:
  def findErrorNums(self, nums: List[int]) -> List[int]:
    ctr = [0] * len(nums)
    for v in nums:
      ctr[v-1] += 1
    ans = [0, 0]
    for i, v in enumerate(ctr):
      if v == 2:
        ans[0] = i+1
      if v == 0:
        ans[1] = i+1
    return ans
