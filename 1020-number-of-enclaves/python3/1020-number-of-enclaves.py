class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
      m = len(grid)
      n = len(grid[0])

      def erase(grid, x, y):
        if x < 0 or x == n or y < 0 or y == m or grid[y][x] == 0: return True
        grid[y][x] = 0
        erase(grid, x, y-1) and erase(grid, x+1, y) and erase(grid, x, y+1) and erase(grid, x-1, y)
        return True

      for x, y in chain(product(range(n), [0, m-1]), product([0, n-1], range(m))):
        if grid[y][x] == 1: erase(grid, x, y)

      return sum(sum(r) for r in grid)