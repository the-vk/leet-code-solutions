class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
      buses = {}
      for x in time:
        buses[x] = buses.get(x, 0) + 1
      l, r = 1, 100000000000000
      while l < r:
        m = (l + r) // 2
        trips = 0
        for bus in buses:
          count = buses[bus]
          trips += (m // bus) * count
        if trips < totalTrips:
          l = m + 1
        else:
          r = m
      return l