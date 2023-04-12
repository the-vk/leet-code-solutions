# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lis = []
        self.dfs(root, lis)
        return lis

    def dfs(self, root, lis):
        if(root == None):
            return
        self.dfs(root.left, lis)
        lis.append(root.val)
        self.dfs(root.right, lis)