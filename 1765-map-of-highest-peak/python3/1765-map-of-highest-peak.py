class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = deque()
        m = len(isWater)
        n = len(isWater[0])
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append((i, j, 0))
                isWater[i][j] = -1
        while q:
            (i, j, h) = q.popleft()
            if not (0 <= i < m and 0 <= j < n and isWater[i][j] == -1):
                continue
            isWater[i][j] = h
            q.append((i-1, j, h+1))
            q.append((i+1, j, h+1))
            q.append((i, j-1, h+1))
            q.append((i, j+1, h+1))
        return isWater