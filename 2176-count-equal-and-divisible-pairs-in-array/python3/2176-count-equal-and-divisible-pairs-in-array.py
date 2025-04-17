class Solution:
  def countPairs(self, nums: List[int], k: int) -> int:
    ctr = {}
    for i, v in enumerate(nums):
      if v not in ctr:
        ctr[v] = []
      ctr[v].append(i)

    ans = 0
    for _, pos in ctr.items():
      for l in range(0, len(pos) - 1):
        for r in range(l+1, len(pos)):
          if (pos[l] * pos[r]) % k == 0:
            ans += 1
    return ans

