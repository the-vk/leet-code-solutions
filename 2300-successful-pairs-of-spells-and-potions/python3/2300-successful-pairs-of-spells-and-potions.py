import math

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
      n = len(spells)
      m = len(potions)
      ans = [0] * n
      potions = sorted(potions)
      for x in range(n):
        t = math.ceil(success / spells[x])
        if t > potions[-1]:
          continue
        if t <= potions[0]:
          ans[x] += m
          continue
        left, right = 0, m
        while left != right:
          mid = (left + right) // 2
          if potions[mid] < t:
            left = mid + 1
          else:
            right = mid
        ans[x] += m - left
      return ans