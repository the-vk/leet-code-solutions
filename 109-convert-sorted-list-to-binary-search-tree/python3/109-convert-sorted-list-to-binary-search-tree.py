# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
      data = []
      while head != None:
        data.append(head.val)
        head = head.next
      return self.build(data, 0, len(data) - 1)

    def build(self, a, l, r):
      if l > r:
        return None
      m = math.ceil((l + r) / 2)
      return TreeNode(a[m], self.build(a, l, m - 1), self.build(a, m + 1, r))