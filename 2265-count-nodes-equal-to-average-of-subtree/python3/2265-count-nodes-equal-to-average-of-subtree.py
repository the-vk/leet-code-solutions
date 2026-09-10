# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def averageOfSubtree(self, root: TreeNode) -> int:
    def walk(root) -> tuple[int, int, int]:
        # (answer, sum, count)
        if None == root:
            return (0, 0, 0)
        a = 0
        s = root.val
        c = 1

        (la, ls, lc) = walk(root.left)
        (ra, rs, rc) = walk(root.right)

        a += la + ra
        s += ls + rs
        c += lc + rc

        if root.val == s // c:
            a += 1

        return (a, s, c)
        
    return walk(root)[0]
