class MedianFinder:

    def __init__(self):
      self.h = []
        

    def addNum(self, num: int) -> None:
      heapq.heappush(self.h, num)
        

    def findMedian(self) -> float:
      self.h.sort()
      if len(self.h) % 2 == 1:
        return self.h[int(len(self.h) // 2)]
      else:
        l = self.h[int(len(self.h) // 2)-1]
        r = self.h[int(len(self.h) // 2)]
        return (l + r) / 2
