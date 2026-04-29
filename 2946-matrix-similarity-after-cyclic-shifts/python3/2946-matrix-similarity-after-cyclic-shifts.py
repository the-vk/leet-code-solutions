class Solution:
  def areSimilar(self, mat: List[List[int]], k: int) -> bool:
    for i in range(len(mat)):
      n = len(mat[i])
      s = k % n
      for j in range(n):
        if mat[i][j] != mat[i][(j+s) % n]:
          return False
    return True
