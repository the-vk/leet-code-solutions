# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        n = len(nums)
        if n == 0:
            return None
        m = n // 2
        r = TreeNode(nums[m])
        if m > 0:
            r.left = self.sortedArrayToBST(nums[:m])
        if m < (n-1):
            r.right = self.sortedArrayToBST(nums[m+1:])
        return r
