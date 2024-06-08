# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def addOneRow(self, root: Optional[TreeNode], val: int, depth: int, l: Optional[TreeNode]=None, r: Optional[TreeNode]=None) -> Optional[TreeNode]:
    if depth == 1:
      if l == None and r == None:
        l = root
      return TreeNode(val, l, r)
    if root == None:
      return None
    root.left = self.addOneRow(root.left, val, depth - 1, root.left, None)
    root.right = self.addOneRow(root.right, val, depth - 1, None, root.right)
    return root