# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
      if not root:
        return True

      queue = [root]
      while queue[0] != None:
        n = queue.pop(0)
        queue.append(n.left)
        queue.append(n.right)
      while queue and queue[0] == None:
        queue.pop(0)
      return not bool(queue)