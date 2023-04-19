# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
      LEFT = True
      RIGHT = False
      self.ans = 0

      def dfs(node, depth, dir):
        if node == None:
          return
        self.ans = max(self.ans, depth)
        dfs(node.left, depth+1 if dir != LEFT else 1, LEFT)
        dfs(node.right, depth+1 if dir != RIGHT else 1, RIGHT) 

      dfs(root, 0, None)
      return self.ans

