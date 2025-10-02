class Solution:
  def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
    full = numBottles
    empty = 0
    drunk = 0
    while full:
      drunk += full
      empty += full
      full = 0
      while empty >= numExchange:
        full += 1
        empty -= numExchange
        numExchange += 1
    return drunk
