class Solution:
  def maxDistance(self, position: List[int], m: int) -> int:
    position = sorted(position)
    l, r = 1, position[-1]
    ans = 1
    while l <= r:
      a = (l+r) // 2
      count = 1
      p = position[0]
      for i in range(1, len(position)):
        if position[i] - p >= a:
          count += 1
          p = position[i]
      if count >= m:
        ans = a
        l = a + 1
      else:
        r = a - 1
    return ans
