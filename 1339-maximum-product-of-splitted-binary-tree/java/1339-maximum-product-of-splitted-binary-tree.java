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
    private static final Long MODULO = 1000000007L;
    public int maxProduct(TreeNode root) {
      var q = new ArrayDeque<TreeNode>();
      q.add(root);
      long total = 0;
      while (!q.isEmpty()) {
        var n = q.poll();
        total += n.val;
        if (n.left != null) {
          q.add(n.left);
        }
        if (n.right != null) {
          q.add(n.right);
        }
      }

      var v = dfs(root, total);
      var ans = v.getValue();
      return (int)(ans % MODULO);
    }

    // sum, ans
    Pair<Long, Long> dfs(TreeNode root, long treeTotal) {
      if (root.left == null && root.right == null) {
        return new Pair<Long, Long>((long)root.val, (long)root.val);
      }

      long sumLeft = 0;
      long sumRight = 0;
      long ans = 0;

      if (root.left != null) {
        var pl = dfs(root.left, treeTotal);
        sumLeft = pl.getKey();
        ans = Math.max(ans, pl.getValue());
      }
      if (root.right != null) {
        var pr = dfs(root.right, treeTotal);
        sumRight = pr.getKey();
        ans = Math.max(ans, pr.getValue());
      }

      var total = sumLeft + root.val + sumRight;

      ans = Math.max(ans, (treeTotal - sumLeft) * sumLeft);
      ans = Math.max(ans, (treeTotal - sumRight) * sumRight);

      return new Pair<>(total, ans);
    }
}
