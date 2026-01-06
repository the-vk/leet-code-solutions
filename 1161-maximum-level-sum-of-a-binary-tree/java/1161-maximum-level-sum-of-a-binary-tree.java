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
  public int maxLevelSum(TreeNode root) {
    var st = new ArrayDeque<Pair<TreeNode, Integer>>();
    st.add(new Pair<>(root, 1));

    var levelSum = new HashMap<Integer, Integer>();

    while (!st.isEmpty()) {
      var n = st.pollFirst();
      var node = n.getKey();
      if (null == node) {
        continue;
      }
      var level = n.getValue();
      levelSum.compute(level, (k, v) -> v == null ? node.val : v + node.val);
      st.add(new Pair<>(node.left, level + 1));
      st.add(new Pair<>(node.right, level + 1));
    }

    Comparator<Map.Entry<Integer, Integer>> bySumDesc = Map.Entry.<Integer, Integer>comparingByValue().reversed();
    Comparator<Map.Entry<Integer, Integer>> byLevelAsc = Map.Entry.<Integer, Integer>comparingByKey();

    return levelSum.entrySet().stream().sorted(
      bySumDesc.thenComparing(byLevelAsc)
    ).findFirst().get().getKey();
  }
}
