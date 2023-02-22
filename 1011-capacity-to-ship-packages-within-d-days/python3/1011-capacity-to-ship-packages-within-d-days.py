class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
      lb = 0
      ub = 0
      for x in weights:
        lb = max(lb, x)
        ub += x
      while lb < ub:
        pc = (lb + ub) // 2
        ships = self.plan(weights, pc)
        if ships > days:
          lb = pc + 1
        else:
          ub = pc
      return lb

    def plan(self, weights, capacity):
      ships = 1
      load = 0
      for x in weights:
        if load + x <= capacity:
          load += x
        else:
          ships += 1
          load = x
      return ships
