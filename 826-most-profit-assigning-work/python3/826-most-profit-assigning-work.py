class Solution:
  def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    jobs = [(profit[x], difficulty[x]) for x in range(len(profit))]
    jobs = sorted(jobs, key=lambda x: x[1])
    jobs = sorted(jobs, key=lambda x: x[0], reverse=True)
    worker = sorted(worker, reverse=True)
    profit = j = w = 0
    while w < len(worker) and j < len(jobs):
      p, d = jobs[j]
      if worker[w] >= d:
        profit += p
        w += 1
      else:
        j += 1
    return profit
