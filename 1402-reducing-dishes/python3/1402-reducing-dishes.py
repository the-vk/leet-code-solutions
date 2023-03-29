class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
      satisfaction = sorted(satisfaction)
      n = len(satisfaction)
      dp = [[0 for _ in range(n)] for _ in range(n)]
      for x in range(n):
        dp[x][x] = satisfaction[x]
        for i in range(x+1, n):
          dp[x][i] = dp[x][i-1] + satisfaction[i] * (i-x+1)
        if x > 0 and dp[x][-1] < dp[x-1][-1]:
          break
      return max([0] + [x[-1] for x in dp])