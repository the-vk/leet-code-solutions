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
  public int minDepth(TreeNode root) {
    if (root == null) {
      return 0;
    }
    if (root.left == null && root.right == null) {
      return 1;
    }

    var dl = minDepth(root.left);
    var dr = minDepth(root.right);

    if (dl != 0 && dr != 0) {
      return 1 + Integer.min(dl, dr);
    }
    if (dl != 0) {
      return 1 + dl;
    }
    return 1 + dr;
  }
}
