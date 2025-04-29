class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
          prereq = {}
          in_count = {}
          for t, f in prerequisites:
            if f not in prereq:
              prereq[f] = set()
            prereq[f].add(t)
            in_count[t] = in_count.get(t, 0) + 1
          for v in range(numCourses):
            if v not in in_count:
              in_count[v] = 0
          q = []
          for v, c in in_count.items():
            heapq.heappush(q, (c, v))
          taken = set()
          while q:
            c, v = heapq.heappop(q)
            if v in taken:
              continue
            if c != 0:
              return False
            taken.add(v)
            for nc in prereq.get(v, []):
              in_count[nc] -= 1
              heapq.heappush(q, (in_count[nc], nc))
          return True