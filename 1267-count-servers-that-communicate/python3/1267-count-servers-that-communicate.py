class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rows = {}
        cols = {}
        serv = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if i not in rows:
                    rows[i] = set()
                if j not in cols:
                    cols[j] = set()
                s = (i, j)
                serv.add(s)
                rows[i].add(s)
                cols[j].add(s)
        ans = len(serv)
        while serv:
            (i, j) = serv.pop()
            if len(rows[i]) == 1 and len(cols[j]) == 1:
                ans -= 1
        return ans

        