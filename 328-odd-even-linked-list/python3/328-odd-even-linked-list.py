# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
      return None
    i = 0
    odd_tail = head
    even_head = head.next
    even_tail = even_head
    n = even_tail
    while n:
      i += 1
      if i % 2 == 0:
        even_tail.next = n.next
        if not even_tail.next:
          break
        even_tail = even_tail.next
      else:
        odd_tail.next = n.next
        if not odd_tail.next:
          break
        odd_tail = odd_tail.next
      n = n.next
    odd_tail.next = even_head
    return head