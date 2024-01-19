class Solution:
  def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    def clamp(v, vMin, vMax):
      return min(max(v, vMin), vMax)

    n = len(matrix)
    dp = [[100*100+1] * n for _ in range(n)]
    for i in range(n):
      dp[0][i] = matrix[0][i]
    for row in range(1, n):
      for col in range(n):
        for off in [-1,0,1]:
          dp[row][col] = min(dp[row][col], dp[row-1][clamp(col+off, 0, n-1)] + matrix[row][col])
    return min(dp[-1])
        