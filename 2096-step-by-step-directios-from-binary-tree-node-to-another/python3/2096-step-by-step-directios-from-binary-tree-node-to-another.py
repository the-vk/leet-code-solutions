class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(node, p, q):
            if not node or node.val == p or node.val == q:
                return node
            left = lca(node.left, p, q)
            right = lca(node.right, p, q)
            if left and right:
                return node
            return left if left else right

        def find_path(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            if find_path(node.left, target, path):
                path.append('L')
                return True
            if find_path(node.right, target, path):
                path.append('R')
                return True
            return False

        # Find the lowest common ancestor
        lca_node = lca(root, startValue, destValue)

        # Find paths from LCA to start and destination
        start_path, dest_path = [], []
        find_path(lca_node, startValue, start_path)
        find_path(lca_node, destValue, dest_path)

        # Construct the final path
        return 'U' * len(start_path) + ''.join(dest_path[::-1])