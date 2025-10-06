class Solution:
  def swimInWater(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    dirs = [
      [-1, 0],
      [0 , 1],
      [1 , 0],
      [0 ,-1]
    ]
    q = [(grid[0][0], 0, 0)]
    seen = set()
    while q:
      t, i, j = heapq.heappop(q)
      if i == (m-1) and j == (n-1):
        return t
      if (i, j) in seen:
        continue
      seen.add((i, j))
      for di, dj in dirs:
        if 0 <= i + di < m and 0 <= j + dj < n:
          heapq.heappush(q, (max(t, grid[i + di][j + dj]), i + di, j + dj))
    return -1

