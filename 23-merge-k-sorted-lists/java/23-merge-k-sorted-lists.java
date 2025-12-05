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
  public ListNode mergeKLists(ListNode[] lists) {
    var queue = new PriorityQueue<ListNode>(Comparator.comparing(v -> v.val));
    for (var n : lists) {
      if (n != null) {
        queue.add(n);
      }
    }

    ListNode result = queue.peek();
    ListNode node = null;
    while (!queue.isEmpty()) {
      var n = queue.poll();
      if (null != n.next) {
        queue.add(n.next);
      }
      if (null == node) {
        node = n;
      } else {
        node.next = n;
        node = node.next;
      }
      
      n.next = null;
    }

    return result;
  }
}