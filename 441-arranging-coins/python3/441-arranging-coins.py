class Solution:
  def arrangeCoins(self, n: int) -> int:
    return math.floor((-1 + math.sqrt(1 + n * 8)) / 2)

