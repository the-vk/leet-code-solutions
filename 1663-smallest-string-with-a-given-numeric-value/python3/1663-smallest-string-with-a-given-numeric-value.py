class Solution:
  def getSmallestString(self, n: int, k: int) -> str:
    A = 1
    Z = ord('z') - ord('a') + 1
    ans = [1] * n
    i = n - 1
    k -= n
    while k > 0:
      tmp = min(k, Z-1)
      ans[i] += tmp
      k -= tmp
      i -= 1
    return ''.join([chr(v + ord('a') - 1) for v in ans])
