class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
      projects = [ (capital[i], profits[i]) for i in range(len(profits))]
      # sort: capital asc, profit desc
      projects.sort(key=itemgetter(1), reverse=True)
      projects.sort(key=itemgetter(0))

      i = 0
      x = 0
      xpos = 0
      queue = []
      while k > 0 and i < len(projects):
        cap, prof = projects[i]
        i += 1
        if cap <= w:
          # Add projects to the queue
          if cap != x:
            xpos = 0
            x = cap
          while xpos < len(queue) and prof < queue[xpos]:
            xpos += 1
          queue.insert(xpos, prof)
        else:
          # Pop projects from the queue
          while w < cap and k > 0 and len(queue) > 0:
            w += queue.pop(0)
            k -= 1
          if cap <= w:
            if cap != x:
              xpos = 0
              x = cap
            while xpos < len(queue) and prof < queue[xpos]:
              xpos += 1
            queue.insert(xpos, prof)
      while k > 0 and len(queue) > 0:
        w += queue.pop(0)
        k -= 1
      return w
