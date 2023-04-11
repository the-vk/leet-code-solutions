# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      tail = head
      head = None
      while tail:
        n = tail.next
        tail.next = head
        head = tail
        tail = n
      return head