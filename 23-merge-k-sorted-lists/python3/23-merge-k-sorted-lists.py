# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      lists = [x for x in lists if x != None]
      if len(lists) == 0:
        return None
      ans = lists[0]
      rest = lists[1:]
      
      for r in rest:
        if r == None:
          next
        l = ans
        if l.val > r.val:
          l, r = r, l
        ans = l
        l = l.next
        w = ans
        while l != None and r != None:
          if l.val <= r.val:
            w.next = l
            l = l.next
          else:
            w.next = r
            r = r.next
          w = w.next
        if l == None and r != None:
          w.next = r
        if l != None and r == None:
          w.next = l

      return ans