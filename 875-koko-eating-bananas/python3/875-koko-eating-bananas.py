class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      l, r = 1, max(piles)

      while l < r:
        speed = (l + r) // 2
        time = 0
        for p in piles:
          time += (p + speed - 1) // speed
        if time <= h:
          r = speed
        else:
          l = speed + 1
      return l