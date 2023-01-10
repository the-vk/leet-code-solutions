# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        m = dict()
        stack = list()
        stack.append(root)
        while len(stack) > 0:
            n = stack.pop()
            if n.left != None:
                stack.append(n.left)
            if n.right != None:
                stack.append(n.right)
            if n.val not in m:
                m[n.val] = 1
            else:
                m[n.val] += 1
        mv = max(m.values())
        modes = []
        for k, v in m.items():
            if v == mv:
                modes.append(k)
        return modes