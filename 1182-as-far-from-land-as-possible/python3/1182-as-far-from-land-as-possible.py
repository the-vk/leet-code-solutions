class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                adj = self.adjacent(i, j, n)
                for ii, jj in adj:
                    if grid[ii][jj] == 0:
                        queue.append((ii, jj, -1))
        if not queue:
            return -1

        ans = 0
        while queue:
            i, j, d = queue.pop(0)
            if grid[i][j] != 0 and d <= grid[i][j]:
                continue
            grid[i][j] = d
            ans = min(ans, d)
            adj = self.adjacent(i, j, n)
            for ii, jj in adj:
                if grid[ii][jj] == 1:
                    continue
                queue.append((ii, jj, d - 1))
        return ans * -1            
        
    def adjacent(self, i, j, n):
        res = []
        # top
        if j > 0:
            res.append((i, j - 1))
        # right
        if i < n - 1:
            res.append((i + 1, j))
        # bottom
        if j < n - 1:
            res.append((i, j + 1))
        # left
        if i > 0:
            res.append((i - 1, j))
        return res