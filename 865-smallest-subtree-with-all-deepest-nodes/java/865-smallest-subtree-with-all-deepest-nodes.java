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
  public TreeNode subtreeWithAllDeepest(TreeNode root) {
    return dfs(root, 0).getValue();
  }

  Pair<Integer, TreeNode> dfs(TreeNode root, int depth) {
    if (null == root.left && null == root.right) {
      return new Pair<>(depth, root);
    }

    Pair<Integer, TreeNode> leftDfs = root.left == null ? null : dfs(root.left, depth + 1);
    Pair<Integer, TreeNode> rightDfs = root.right == null ? null : dfs(root.right, depth + 1);

    if (leftDfs != null && rightDfs != null) {
      if (leftDfs.getKey() == rightDfs.getKey()) {
        return new Pair<>(leftDfs.getKey(), root);
      }

      return leftDfs.getKey() > rightDfs.getKey() ? leftDfs : rightDfs;
    }

    return leftDfs != null ? leftDfs : rightDfs;
  }
}
