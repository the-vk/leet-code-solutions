"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
      return self.recurse(grid, 0, 0, len(grid))

    def recurse(self, grid, i, j, s):
      if s == 1:
        return Node(grid[i][j] == 1, True, None, None, None, None)

      s //= 2
      topLeft = self.recurse(grid, i, j, s)
      topRight = self.recurse(grid, i, j + s, s)
      bottomLeft = self.recurse(grid, i + s, j, s)
      bottomRight = self.recurse(grid, i + s, j + s, s)

      allLeaf = topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf
      allSameVal = topLeft.val == topRight.val and topRight.val == bottomLeft.val and bottomLeft.val == bottomRight.val

      if allLeaf and allSameVal:
        return Node(topLeft.val, True, None, None, None, None)
      else:
        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
