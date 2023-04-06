class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
      ans = 0
      for y in range(len(grid)):
        for x in range(len(grid[y])):
          if grid[y][x] == 0 and self.isClosed(grid, x, y):
            ans += 1
      return ans

    def isClosed(self, grid, x, y):
      grid[y][x] = -1
      closed = True
      if x == 0 or x == (len(grid[y])-1) or y == 0 or y == (len(grid)-1):
        closed = False
      # top
      if y > 0 and grid[y-1][x] == 0:
        closed = self.isClosed(grid, x, y-1) & closed
      # right
      if x < (len(grid[y])-1) and grid[y][x+1] == 0:
        closed = self.isClosed(grid, x+1, y) & closed
      # bottom
      if y < (len(grid)-1) and grid[y+1][x] == 0:
        closed = self.isClosed(grid, x, y+1) & closed
      # left
      if x > 0 and grid[y][x-1] == 0:
        closed = self.isClosed(grid, x-1, y) & closed
      if not closed:
        grid[y][x] = -2
      return closed