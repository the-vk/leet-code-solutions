/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
      var answer = new ArrayList<Integer>();
      if (null == root) {
        return answer;
      }
      var s = new ArrayDeque<TreeNode>();
      s.add(root);

      while (!s.isEmpty()) {
        var n = s.pollLast();
        if (null == n) {
          continue;
        }
        answer.add(n.val);
        if (null != n.right) {
          s.add(n.right);
        }
        if (null != n.left) {
          s.add(n.left);
        }
      }

      return answer;
    }
}
