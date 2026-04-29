class Solution:
  def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
    M = len(grid)
    N = len(grid[0])
    MD = 12345

    ans = [[0] * N for _ in range(M)]
    pref, sufx = 1, 1

    for i in range(M):
      for j in range(N):
        ans[i][j] = pref
        pref = pref * grid[i][j] % MD

    for i in range(M-1, -1, -1):
      for j in range(N-1, -1, -1):
        ans[i][j] = ans[i][j] * sufx % MD
        sufx = sufx * grid[i][j] % MD

    return ans
        
