class Solution:
  def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    def area(x1, y1, x2, y2):
      return (x2-x1) * (y2-y1)
    
    ans = area(ax1, ay1, ax2, ay2) + area(bx1, by1, bx2, by2)
    x1 = x2 = y1 = y2 = None
    if ax1 <= bx1 <= ax2:
      x1 = bx1
    if bx1 <= ax1 <= bx2:
      x1 = ax1
    if ax1 <= bx2 <= ax2:
      x2 = bx2
    if bx1 <= ax2 <= bx2:
      x2 = ax2
    if ay1 <= by1 <= ay2:
      y1 = by1
    if by1 <= ay1 <= by2:
      y1 = ay1
    if ay1 <= by2 <= ay2:
      y2 = by2
    if by1 <= ay2 <= by2:
      y2 = ay2
    if x1 != None and x2 != None and y1 != None and y2 != None:
      ans -= area(x1, y1, x2, y2)
    return ans