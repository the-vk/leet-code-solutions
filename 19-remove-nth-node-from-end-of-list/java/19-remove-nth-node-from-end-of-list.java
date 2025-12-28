/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
  public ListNode removeNthFromEnd(ListNode head, int n) {
    var queue = new ArrayDeque<ListNode>();
    var res = head;
    while (null != head) {
      while (queue.size() > n) {
        queue.pollFirst();
      }

      queue.add(head);
      head = head.next;
    }

    if (queue.size() == n) {
      queue.pollFirst();
      res = queue.peekFirst();
    } else {
      var node = queue.pollFirst();
      var to_delete = queue.pollFirst();
      node.next = to_delete.next;
    }

    return res;
  }
}
