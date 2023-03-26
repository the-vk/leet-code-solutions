class Solution:
    def longestCycle(self, edges: List[int]) -> int:
      inbound = [set() for _ in range(len(edges))]
      for i, x in enumerate(edges):
        inbound[x].add(i)
      for i, x in enumerate(edges):
        n = i
        while len(inbound[n]) == 0:
          if edges[n] == -1:
            break
          inbound[edges[n]].discard(n)
          ni = edges[n]
          edges[n] = -1
          n = ni
        if x == -1:
          queue = list(inbound[i])
          while queue:
            n = queue.pop()
            if edges[n] == -1:
              continue
            edges[n] = -1
            queue = queue + list(inbound[n])
      ans = -1
      l = 0
      for i in range(len(edges)):
        if edges[i] == -1:
          continue
        n = i
        l = 0
        while edges[n] != -1:
          l += 1
          ni = edges[n]
          edges[n] = -1
          n = ni
        ans = max(ans, l)
      return ans