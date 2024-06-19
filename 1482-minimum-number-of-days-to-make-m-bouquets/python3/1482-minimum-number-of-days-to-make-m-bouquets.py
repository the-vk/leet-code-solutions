class Solution:
  def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
    if len(bloomDay) < m*k:
      return -1
    l = 1
    r = max(bloomDay)
    while l < r:
      d = (l + r) // 2
      flowers = 0
      bouquets = 0
      for x in bloomDay:
        if x <= d:
          flowers += 1
          if flowers == k:
            bouquets += 1
            flowers = 0
        else:
          flowers = 0
      if bouquets >= m:
        r = d
      else:
        l = d + 1
    return l

        