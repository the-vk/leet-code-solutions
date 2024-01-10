# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
      def walk(root, adjacent):
        if root.left:
          adjacent[root.val].add(root.left.val)
          adjacent[root.left.val].add(root.val)
          walk(root.left, adjacent)
        if root.right:
          adjacent[root.val].add(root.right.val)
          adjacent[root.right.val].add(root.val)
          walk(root.right, adjacent)
        return adjacent
      def infect(c, i, adjacent):
        if c in i:
          return 0
        i.add(c)
        nn = adjacent[c]
        if len(nn) == 0:
          return 1
        t = 0
        for n in nn:
          t = max(t, infect(n, i, adjacent))
        return t + 1
      adjacent = walk(root, defaultdict(set))
      return infect(start, set(), adjacent) - 1

        