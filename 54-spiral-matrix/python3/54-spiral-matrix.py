class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    m = len(matrix)
    n = len(matrix[0])
    ans = [0] * (m * n)
    dirs = [
      [0, 1],
      [1, 0],
      [0, -1],
      [-1, 0]
    ]
    di = 0
    i = 0
    seen = set()
    r, c = 0, 0
    while True:
      ans[i] = matrix[r][c]
      seen.add((r, c))
      i += 1
      if i == len(ans):
        return ans
      tries = 0
      while tries < 4:
        tries += 1
        dr, dc = dirs[di]
        nr, nc = r + dr, c + dc
        if (0 <= nr < m) and (0 <= nc < n) and (nr, nc) not in seen:
          r, c = nr, nc
          break
        di = (di + 1) % 4
      if tries == 4:
        return ans
