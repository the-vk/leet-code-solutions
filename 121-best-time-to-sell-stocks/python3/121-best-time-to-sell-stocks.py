class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      min_price = float("inf")
      profit = 0
      for x in prices:
        min_price = min(min_price, x)
        if x > min_price:
          profit = max(profit, x - min_price)
      return profit