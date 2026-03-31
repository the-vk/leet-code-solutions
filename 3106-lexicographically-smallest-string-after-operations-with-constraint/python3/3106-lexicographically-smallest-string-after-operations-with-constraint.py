class Solution:
  def getSmallestString(self, s: str, k: int) -> str:
    n = len(s)

    A = ord('a')
    Z = ord('z')
    ZN = Z - A

    def distance_chr(a, b) -> int:
      return min(
        abs(a - b),
        ZN - abs(a - b) + 1
      )

    def distance(a, b) -> int:
      return sum([distance_chr(a[i], b[i]) for i in range(n)]) 
    
    t = [A] * n
    s = [ord(v) for v in s]
    overflow = Z + 1
    while distance(s, t) > k:
      for x in range(n-1, -1, -1):
        t[x] += 1
        if t[x] != overflow:
          break
        t[x] = A
    return ''.join([chr(v) for v in t])
