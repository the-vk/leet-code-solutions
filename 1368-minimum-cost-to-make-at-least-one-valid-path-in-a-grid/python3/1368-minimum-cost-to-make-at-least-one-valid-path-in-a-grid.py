class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        def calc_edge(i, j, op):
            if op == 1:
                return (i, j+1, 0 if grid[i][j] == op else 1)
            if op == 2:
                return (i, j-1, 0 if grid[i][j] == op else 1)
            if op == 3:
                return (i+1, j, 0 if grid[i][j] == op else 1)
            if op == 4:
                return (i-1, j, 0 if grid[i][j] == op else 1)
            return None
        m = len(grid)
        n = len(grid[0])
        graph = {}
        for i in range(m):
            for j in range(n):
                graph[(i, j)] = []
                for o in range(1, 5):
                    edge = calc_edge(i, j, o)
                    if (0 <= edge[0] < m) and (0 <= edge[1] < n):
                        graph[(i, j)].append(edge)
                graph[(i, j)].sort(key=itemgetter(2))
        print(graph)
        q = deque([(0, 0, 0)])
        visited = set()
        while q:
            (i, j, c) = q.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if i == (m-1) and j == (n-1):
                return c
            nc = graph[(i, j)]
            for x in nc:
                if x[2] == 0:
                    q.appendleft((x[0], x[1], c + x[2]))
                else:
                    q.append((x[0], x[1], c + x[2]))
        return -1
