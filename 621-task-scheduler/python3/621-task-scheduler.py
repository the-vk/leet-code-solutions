class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
      ctr = Counter(tasks)
      q = []
      # [-ct, cd, t]
      for t, c in ctr.items():
        heapq.heappush(q, [-c, 0, t])
      ans = 0
      while q:
        skipped = []
        t = None
        while q:
          t = heapq.heappop(q)
          if t[1] > 0:
            skipped.append(t)
            t = None
            continue
          else:
            break
        if t != None:
          t[0] += 1
          t[1] = n + 1
          if t[0] != 0:
            heapq.heappush(q, t)
        
        for s in skipped:
          heapq.heappush(q, s)
        for s in q:
          s[1] = max(0, s[1]-1)
        ans += 1
        
      return ans
