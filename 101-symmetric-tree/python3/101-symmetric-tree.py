# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      return self.isEqual(root.left, root.right)

    def isEqual(self, left, right) -> bool:
      if left == None or right == None:
        return left == right
      if left.val != right.val:
        return False
      return self.isEqual(left.left, right.right) and self.isEqual(left.right, right.left)
