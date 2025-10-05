class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    m = len(heights)
    n = len(heights[0])

    dirs = [
      [-1, 0], # up
      [0, 1], # right
      [1, 0], # down
      [0, -1], # left
    ]

    def work(q, s):
      while q:
        [l, c] = q.pop(0)
        pair = (l, c)
        if pair in s:
          continue
        s.add(pair)
        for lo, co in dirs:
          nl = l + lo
          nc = c + co
          if not (0 <= nl < m):
            continue
          if not (0 <= nc < n):
            continue
          if heights[l][c] <= heights[nl][nc]:
            q.append([nl, nc])
      
    pacific_queue = [[0, v] for v in range(n)] + [[v, 0] for v in range(m)]
    atlantic_queue =[[m-1, v] for v in range(n)] + [[v, n-1] for v in range(m)]

    pacific = set()
    atlantic = set()

    work(pacific_queue, pacific)
    work(atlantic_queue, atlantic)

    return [[l, c] for (l, c) in pacific & atlantic]
