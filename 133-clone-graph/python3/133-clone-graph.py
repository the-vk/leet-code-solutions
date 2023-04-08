"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
      if node == None:
        return None

      orig = {}
      copy = {}
      adj = defaultdict(list)

      def deepClone(node):
        if node == None or node.val in orig:
          return
        orig[node.val] = node
        copy[node.val] = Node(node.val)
        for x in node.neighbors:
          adj[node.val].append(x.val)
          deepClone(x)

      deepClone(node)
      for k in adj:
        n = copy[k]
        for x in adj[k]:
          n.neighbors.append(copy[x])
      
      return copy[1]
