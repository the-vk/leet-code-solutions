# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
      stack = []
      res = float("inf")
      prev = None
      while root != None or len(stack) > 0:
        if root != None:
          stack.append(root)
          root = root.left
        else:
          node = stack.pop()
          if prev != None:
            res = min(res, node.val - prev.val)
          prev = node
          root = node.right
      return res
