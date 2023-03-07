# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      postorder = []
      return self.traverse(root, postorder)

    def traverse(self, root, postorder):
      if root == None:
        return None
      self.traverse(root.left, postorder)
      self.traverse(root.right, postorder)
      postorder.append(root.val)
      return postorder
