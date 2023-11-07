import math

class RecentCounter:

    def __init__(self):
      self.queue = []
        
    def ping(self, t: int) -> int:
      self.queue.append(t)
      l, r = 0, len(self.queue) - 1
      while l < r:
        m = math.floor((l+r)/2)
        if self.queue[-1] - self.queue[m] <= 3000:
          r = m
        else:
          l = m + 1
      self.queue = self.queue[l:]
      return len(self.queue)
