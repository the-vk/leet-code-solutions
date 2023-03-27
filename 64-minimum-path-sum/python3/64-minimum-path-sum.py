class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
      m = len(grid)
      n = len(grid[0])
      for x in range(min(m, n)):
        row = x
        col = x
        # update row
        for c in range(x, n):
          v = grid[row][c]
          opts = []
          if c > 0:
            opts.append(v + grid[row][c - 1])
          if row > 0:
            opts.append(v + grid[row-1][c])
          if opts:
            grid[row][c] = min(opts)
        # update column
        for r in range(x+1, m):
          v = grid[r][col]
          opts = []
          if r > 0:
            opts.append(v + grid[r-1][col])
          if col > 0:
            opts.append(v + grid[r][col-1])
          if opts:
            grid[r][col] = min(opts)
      return grid[m-1][n-1]