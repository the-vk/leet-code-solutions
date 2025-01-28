class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))
            res = 0
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                res += dfs(r+d[0], c+d[1])
            return res + grid[r][c]

        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j))
        return res