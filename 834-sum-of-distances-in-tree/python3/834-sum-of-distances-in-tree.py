class Solution:
  def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
    def dfs(adj, n, node, prev, height, subtree):
      subtree[node] += 1
      for e in adj[node]:
        if e != prev:
          height[e] = 1 + height[node]
          dfs(adj, n, e, node, height, subtree)
          subtree[node] += subtree[e]

    def rec(adj, n, node, prev, subtree, dp):
      for e in adj[node]:
        if e != prev:
          dp[e] = dp[node] - subtree[e] + (n-subtree[e])
          rec(adj, n, e, node, subtree, dp)

    adj = [set() for _ in range(n)]
    for (l, r) in edges:
      adj[l].add(r)
      adj[r].add(l)
    height = [0] * n
    subtree = [0] * n
    dp = [0] * n
    dfs(adj, n, 0, -1, height, subtree)
    for i in range(n):
      dp[0] += height[i]
    rec(adj, n, 0, -1, subtree, dp)
    return dp
