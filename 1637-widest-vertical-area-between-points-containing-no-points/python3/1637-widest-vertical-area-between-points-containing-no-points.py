class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted([v[0] for v in points])
        area = [0] * (len(points)-1)
        for i in range(len(area)):
          area[i] = points[i+1] - points[i]
        return max(area)