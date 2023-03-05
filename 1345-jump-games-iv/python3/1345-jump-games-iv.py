class Solution:
    def minJumps(self, arr: List[int]) -> int:
      edges = {}
      n = len(arr)
      for i, v in enumerate(arr):
        ls = edges.get(v, [])
        ls.append(i)
        edges[v] = ls
      queue = deque()
      queue.append((0, 0))
      visited = set()
      while queue:
        i, s = queue.popleft()
        if i == n - 1:
          return s
        for ni in edges[arr[i]]:
          if ni not in visited:
            queue.append((ni, s + 1))
            visited.add(ni)
        edges[arr[i]] = []

        if i > 0 and (i-1) not in visited:
          queue.append((i-1, s+1))
          visited.add(i-1)
        if (i+1) not in visited:
          queue.append((i+1, s+1))
          visited.add(i+1)
      return -1
