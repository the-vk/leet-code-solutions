/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
  public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    var l = Math.min(p.val, q.val);
    var h = Math.max(p.val, q.val);

    while (root != null) {
      if ((l < root.val && h > root.val) || (l == root.val || h == root.val)) {
        return root;
      }

      if (h < root.val) {
        root = root.left;
      }

      if (l > root.val) {
        root = root.right;
      }
    }

    return null;
  }
}

