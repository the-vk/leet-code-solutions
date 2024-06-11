# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
      while head and head.val == val:
        head = head.next
      n = head
      while n:
        if n.next and n.next.val == val:
          n.next = n.next.next
        else:
          n = n.next
      return head
