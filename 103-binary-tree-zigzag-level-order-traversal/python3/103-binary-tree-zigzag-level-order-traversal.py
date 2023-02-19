# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      res = []
      queue = [(root, 0)]
      while queue:
        n, l = queue.pop(0)
        if n == None:
          continue
        if l == len(res):
          res.append([])
        res[l].append(n.val)
        queue.extend([(n.left, l + 1), (n.right, l + 1)])
      for i in range(1, len(res), 2):
        res[i].reverse()
      return res
