class Solution:
  def getSmallestString(self, s: str, k: int) -> str:
    t = [ord(v) for v in s]
    n = len(t)
    for i in range(n):
      left = t[i] - ord('a')
      right = ord('z') - t[i] + 1
      md = min(left, right)
      if k >= md:
        k -= md
        t[i] = ord('a')
      else:
        t[i] -= k
        break
    return ''.join([chr(v) for v in t]
