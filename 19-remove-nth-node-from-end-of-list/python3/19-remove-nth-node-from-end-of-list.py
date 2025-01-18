# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return None
        st = []
        while head:
            st.append(head)
            head = head.next
        tail = None
        while n > 1:
            tail = st.pop()
            n -= 1
        nth = st.pop()
        nth.next = None
        if st:
            st[-1].next = tail
        return st[0] if st else tail
