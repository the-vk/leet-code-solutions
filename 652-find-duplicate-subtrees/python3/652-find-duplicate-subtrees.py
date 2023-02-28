# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
      # val -> TreeNode
      roots = {}

      st = [root]
      while st:
        n = st.pop()
        if n == None:
          continue
        l = roots.get(n.val, [])
        l.append(n)
        roots[n.val] = l
        st.extend([n.right, n.left])

      ans = []
      memo = {}
      for k in roots:
        nodes = roots[k]
        i = 0
        while i < (len(nodes) - 1):
          j = i + 1
          found = False
          while j < len(nodes):        
            if self.eql(nodes[i], nodes[j], memo):
              if not found:
                found = True
                ans.append(nodes[i])
              nodes.pop(j)
            else:
              j += 1
          i += 1
            
      return ans

    def eql(self, left, right, memo):
      k = (left, right)
      if k not in memo:
        if left == right:
          memo[k] = True
        elif left == None or right == None:
          memo[k] = False
        elif left.val != right.val:
          memo[k] = False
        else:
          memo[k] = self.eql(left.left, right.left, memo) and self.eql(left.right, right.right, memo)

      return memo[k]
