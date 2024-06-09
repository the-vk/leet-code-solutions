class Solution:
  def rangeBitwiseAnd(self, left: int, right: int) -> int:
    p = 0
    ans = 0
    while p < 32:
      d = 2 ** p
      l = (left & d) >> p
      r = (right & d) >> p
      if l == r == 1 and (right - left) < d:
        ans += d
      p += 1
    return ans