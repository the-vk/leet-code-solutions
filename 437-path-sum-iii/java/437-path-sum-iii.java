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
  public int pathSum(TreeNode root, int targetSum) {
    var prefix = new HashMap<Long, Integer>(Map.of(0L, 1));

    return dfs(root, 0, targetSum, prefix);
  }

  private int dfs(TreeNode node, long currentSum, int targetSum, Map<Long, Integer> prefix) {
    if (null == node) {
      return 0;
    }

    currentSum += node.val;
    var count = prefix.getOrDefault(currentSum - targetSum, 0);

    prefix.put(currentSum, prefix.getOrDefault(currentSum, 0) + 1);
    count += dfs(node.left, currentSum, targetSum, prefix);
    count += dfs(node.right, currentSum, targetSum, prefix);
    prefix.put(currentSum, prefix.get(currentSum) - 1);

    return count;
  }

