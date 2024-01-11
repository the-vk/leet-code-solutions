# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
      def walk(root, min_v, max_v):
        if not root:
          return None
        if None == min_v:
          min_v = root.val
        if None == max_v:
          max_v = root.val
        max_v = max(max_v, root.val)
        min_v = min(min_v, root.val)
        ans = max(abs(root.val - min_v), abs(root.val - max_v))
        ans_left = walk(root.left, min_v, max_v)
        if ans_left:
          ans = max(ans, ans_left)
        ans_right = walk(root.right, min_v, max_v)
        if ans_right:
          ans = max(ans, ans_right)
        return ans
      return walk(root, None, None)
        