class Solution:
  def hammingWeight(self, n: int) -> int:
    w = 0
    while n > 0:
      if n & 1 == 1:
        w += 1
      n >>= 1
    return w
