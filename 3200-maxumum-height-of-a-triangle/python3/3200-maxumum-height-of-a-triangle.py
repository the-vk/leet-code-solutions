class Solution:
  def maxHeightOfTriangle(self, red: int, blue: int) -> int:
    ans = []
    for balls in [[red, blue], [blue, red]]:
      i = 0
      layer = 0
      layer_size = 0
      while True:
        layer_size += 1
        if layer_size > balls[i]:
          ans.append(layer)
          break
        layer += 1
        balls[i] -= layer_size
        i = (i + 1) % 2
    return max(ans)