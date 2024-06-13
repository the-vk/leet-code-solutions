# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    fast = slow = head
    cnt = 0
    n = head
    while n:
      cnt += 1
      n = n.next
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    if cnt % 2 == 1:
      slow = slow.next
    rev_head = None
    next_head = slow
    while next_head:
      n = next_head.next
      next_head.next = rev_head
      rev_head = next_head
      next_head = n
    while head and rev_head:
      if head.val != rev_head.val:
        return False
      head = head.next
      rev_head = rev_head.next
    return True
