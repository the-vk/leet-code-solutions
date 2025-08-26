class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
      adj = {}
      for l, r in edges:
        if l not in adj:
          adj[l] = set()
        adj[l].add(r)
        if r not in adj:
          adj[r] = set()
        adj[r].add(l)
      q = deque()

      if 1 not in adj:
        return 1.0

      next_nodes = adj[1]
      seen = set()
      seen.add(1)

      for n in next_nodes:
        # next_node, next_t, probability of the next node
        q.appendleft((n, t-1, 1.0 / len(next_nodes)))

      while q:
        next_node, next_t, prob = q.pop()
        if next_t < 0:
          continue

        seen.add(next_node)

        next_nodes = adj[next_node]
        may_be_next_count = 0
        for x in next_nodes:
          if x not in seen:
            may_be_next_count += 1

        if next_node == target and (next_t == 0 or may_be_next_count == 0):
          return prob
          
        for n in next_nodes:
          if n not in seen:
            q.appendleft((n, next_t - 1, prob / may_be_next_count))

      return 0
