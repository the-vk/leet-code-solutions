class Solution(object):
  def connect(self, root):
    """
    :type root: Node
    :rtype: Node
     """

    if root == None:
      return root

    order = []
    q = [(root, 0)]

    while q:
      n, l = q.pop(0)
      order.append((n, l))
      if n.left != None:
        q.append((n.left, l + 1))
      if n.right != None:
        q.append((n.right, l + 1))

    while order:
      n, l = order.pop(0)
      if order and order[0][1] == l:
        n.next = order[0][0]

    return root
       
