class Solution:
  def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
    MODULO = 10**9 + 7
    for l, r, k, v in queries:
      idx = l
      while idx <= r:
        nums[idx] = (nums[idx] * v) % MODULO
        idx += k
    v = 0
    for n in nums:
      v ^= n
    return v
