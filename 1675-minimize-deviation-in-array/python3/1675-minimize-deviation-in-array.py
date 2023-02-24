import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
      pq = [-(x if x % 2 == 0 else x * 2) for x in nums]
      heapq.heapify(pq)
      min_v = -max(pq)
      min_dev = float("inf")
      while True:
        max_v = -heapq.heappop(pq)
        min_dev = min(min_dev, max_v - min_v)
        if max_v % 2 == 1:
          break
        max_v //= 2
        min_v = min(min_v, max_v)
        heapq.heappush(pq, -max_v)
      return min_dev