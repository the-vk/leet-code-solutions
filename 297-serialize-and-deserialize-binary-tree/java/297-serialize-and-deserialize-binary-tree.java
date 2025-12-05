/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
  public String serialize(TreeNode root) {
    if (root == null) {
      return "[]";
    }

    var tokens = new ArrayList<String>();

    var queue = new ArrayDeque<Optional<TreeNode>>();
    queue.add(Optional.of(root));

    while (queue.size() > 0) {
      var no = queue.poll();
      if (no.isEmpty()) {
        tokens.add("null");
      } else {
        var n = no.get();
        tokens.add(Integer.toString(n.val));
        queue.add(Optional.ofNullable(n.left));
        queue.add(Optional.ofNullable(n.right));
      }
    }

    while ("null".equals(tokens.get(tokens.size() - 1))) {
     tokens.remove(tokens.size() - 1);
    }

    return String.format("[%s]", String.join(",", tokens));
  }

  // Decodes your encoded data to tree.
  public TreeNode deserialize(String data) {
    if ('[' != data.charAt(0) && ']' != data.charAt(data.length() - 1)) {
      throw new IllegalArgumentException();
    }
    data = data.substring(1, data.length() - 1);
    var tokens = data.split(",");

    if (tokens.length == 0 || tokens[0].length() == 0 || tokens[0] == "null") {
      return null;
    }

    var root = new TreeNode(Integer.valueOf(tokens[0]));

    Deque<TreeNode> queue = new ArrayDeque<>();
    queue.add(root);

    for (var i = 1; i < tokens.length; i += 2) {
      var left = tokens[i];
      var node = queue.poll();

      if ("null".equals(left)) {
        node.left = null;
      } else {
        node.left = new TreeNode(Integer.valueOf(left));
        queue.add(node.left);
      }

      if (i < (tokens.length - 1)) {
        var right = tokens[i+1];

        if ("null".equals(right)) {
          node.right = null;
        } else {
          node.right = new TreeNode(Integer.valueOf(right));
          queue.add(node.right);
        }
      }
    }

    return root;
   }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));