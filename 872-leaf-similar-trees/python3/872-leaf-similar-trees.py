# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
      def leafs(root):
        if root == None:
          return
        if root.left == None and root.right == None:
          yield root.val
        for v in leafs(root.left):
          yield v
        for v in leafs(root.right):
          yield v
      return tuple(leafs(root1)) == tuple(leafs(root2))
        