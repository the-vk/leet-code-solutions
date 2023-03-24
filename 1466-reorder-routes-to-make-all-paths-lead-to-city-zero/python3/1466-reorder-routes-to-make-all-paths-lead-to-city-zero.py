from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
      by_origin = defaultdict(set)
      by_dest = defaultdict(set)
      for origin, dest in connections:
        by_origin[origin].add(dest)
        by_dest[dest].add(origin)
      stack = [0]
      ans = 0
      visited = set()
      while stack:
        n = stack.pop()
        visited.add(n)
        for x in by_origin[n]:
          if x not in visited:
            ans += 1
            by_dest[n].add(x)
        del by_origin[n]
        for x in by_dest[n]:
          if x not in visited:
            stack.append(x)
      return ans