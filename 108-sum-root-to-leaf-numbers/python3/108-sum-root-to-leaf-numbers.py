from math import floor, log, pow

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
      if root == None:
        return 0
      
      arr = []
      self.traverse(root, arr, 0)
      ans = 0
      for x in arr:
        ans += x
      return ans

    def traverse(self, root, arr, v):
      if root == None:
        return
      v *= 10
      v += root.val

      if root.left == None and root.right == None:
        print(v)
        arr.append(v)
      else:
        self.traverse(root.left, arr, v)
        self.traverse(root.right, arr, v)
      