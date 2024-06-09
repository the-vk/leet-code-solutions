class Solution:
  def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    def sol(dp, r, c, moves, m, n):
      if moves < 0:
        return 0
      if r < 0 or c < 0 or r == m or c == n:
        return 1
      ans = 0
      ans += sol(dp, r, c+1, moves - 1, m, n)
      ans += sol(dp, r, c-1, moves - 1, m, n)
      ans += sol(dp, r+1, c, moves - 1, m, n)
      ans += sol(dp, r-1, c, moves - 1, m, n)
      ans = ans % (1e9 + 7)
      dp[r][c][moves] = ans
      return ans

    dp = [[[-1 for _ in range(maxMove + 1)] for _ in range(n)] for _ in range(m)]  
    return sol(dp, startRow, startColumn, maxMove, m, n)  
