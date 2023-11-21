# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def traverse(root, order):
          if root.left != None: traverse(root.left, order)
          order.append(root)
          if root.right != None: traverse(root.right, order)
          return order
        order = traverse(root, [])
        l = -1
        r = len(order)
        for i in range(len(order) - 1):
          if order[i].val > order[i+1].val:
            if l == -1:
              l = i
              break
        for i in range(r-1, l, -1):
          if order[i].val < order[i-1].val:
            r = i
            break
        t = order[l].val
        order[l].val = order[r].val
        order[r].val = t
        return root
