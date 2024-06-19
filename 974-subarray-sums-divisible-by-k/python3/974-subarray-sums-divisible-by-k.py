class Solution:
  def subarraysDivByK(self, nums: List[int], k: int) -> int:
    ans = s = 0
    m = {0: 1}
    for n in nums:
      s += n
      mod = s % k
      if mod < 0:
        mod += k
      if mod in m:
        ans += m[mod]
        m[mod] += 1
      else:
        m[mod] = 1
    return ans