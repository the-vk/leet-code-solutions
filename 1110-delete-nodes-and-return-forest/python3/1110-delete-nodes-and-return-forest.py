# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    st = [root]
    ans = set()
    d = set(to_delete)
    if root.val not in d:
      ans.add(root)
    while st:
      n = st.pop()
      if n == None:
        continue
      if n.val in d:
        ans.add(n.left)
        ans.add(n.right)
      if n.left:
        st.append(n.left)
        if n.left.val in d:
          ans.add(n.left.left)
          ans.add(n.left.right)
          st.append(n.left.left)
          st.append(n.left.right)
          n.left = None
      if n.right:
        st.append(n.right)
        if n.right.val in d:
          ans.add(n.right.left)
          ans.add(n.right.right)
          st.append(n.right.left)
          st.append(n.right.right)
          n.right = None
    return [x for x in ans if x != None and x.val not in d]
