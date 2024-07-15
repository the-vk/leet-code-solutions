# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
    roots = set()
    children = set()
    nodes = {}
    for (p, c, l) in descriptions:
      if p not in children:
        roots.add(p)
      roots.discard(c)
      children.add(c)
      if p not in nodes:
        nodes[p] = TreeNode(p)
      if c not in nodes:
        nodes[c] = TreeNode(c)
      if l == 0:
        nodes[p].right = nodes[c]
      else:
        nodes[p].left = nodes[c]
    return nodes[roots.pop()]
