class Solution:
  def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    red = {}
    blue = {}
    for h, e in [[red, redEdges], [blue, blueEdges]]:  
      for f, t in e:
        if f not in h:
          h[f] = []
        h[f].append(t)

    ans_r = [-1] * n
    ans_b = [-1] * n
    queue = [(0, 0, red, ans_r, blue, ans_b), (0, 0, blue, ans_b, red, ans_r)]
    while queue:
      f, d, cc, ans, nc, n_ans = queue.pop(0)
      if ans[f] != -1 and ans[f] < d:
        continue
      ans[f] = d
      for t in nc.get(f, []):
        queue.append((t, d + 1, nc, n_ans, cc, ans))
    
    for i in range(n):
      rd = ans_r[i]
      bd = ans_b[i]
      if rd == -1:
        ans_r[i] = bd
      elif bd == -1:
        ans_r[i] = rd
      else:
        ans_r[i] = min(rd, bd)
    return ans_r
    