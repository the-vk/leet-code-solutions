class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
      n = len(s)
      dp = [0] * n
      for i in range(n-1, -1, -1):
        ndp = [0] * n
        ndp[i] = 1
        for j in range(i+1, n):
          if s[i] == s[j]:
            ndp[j] = 2 + dp[j-1]
          else:
            ndp[j] = max(dp[j], ndp[j-1])
        dp = ndp
      return dp[-1]