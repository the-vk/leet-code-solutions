class Solution:
  def judgeSquareSum(self, c: int) -> bool:
    root = int(math.sqrt(c))
    sqrs = [0] * (root + 1)
    for i in range(0, root+1):
      sqrs[i] = i**2
    l = 0
    r = len(sqrs) - 1
    while l <= r:
      s = sqrs[l] + sqrs[r]
      if s == c:
        return True
      if s < c:
        l += 1
      else:
        r -= 1
    return False