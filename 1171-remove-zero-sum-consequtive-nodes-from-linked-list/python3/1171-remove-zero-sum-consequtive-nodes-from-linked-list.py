# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
    ps = 0
    psm = {}
    root = ListNode(0, head)
    c = root
    while c:
      ps += c.val
      if ps in psm:
        ss = psm[ps]
        se = ss.next
        cs = ps + (se.val if se else 0)
        while cs != ps:
          del psm[cs]
          se = se.next
          cs += se.val if se else 0
        ss.next = c.next
      else:
        psm[ps] = c
      c = c.next
    return root.next
