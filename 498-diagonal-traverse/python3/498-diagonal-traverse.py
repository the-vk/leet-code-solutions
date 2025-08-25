class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        if m == 0:
          return []

        n = len(mat[0])
        if n == 0:
          return []

        ans = []

        x = y = 0

        while x < m and y < n:
          ans.append(mat[x][y])

          if (x + y) % 2 == 1:
            if x == (m-1):
              y += 1
            elif y == 0:
              x += 1
            else:
              x += 1
              y -= 1
          else:
            if y == (n-1):
              x += 1
            elif x == 0:
              y += 1
            else:
              x -= 1
              y += 1
        return ans
