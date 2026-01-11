/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
  public boolean hasCycle(ListNode head) {
    if (head == null) {
      return false;
    }
    var fast = head.next;
    var slow = head;

    while (true) {
      if (fast == null || fast.next == null || slow == null) {
        return false;
      }

      if (fast == slow) {
        return true;
      }

      fast = fast.next.next;
      slow = slow.next;
    }
  }
}
