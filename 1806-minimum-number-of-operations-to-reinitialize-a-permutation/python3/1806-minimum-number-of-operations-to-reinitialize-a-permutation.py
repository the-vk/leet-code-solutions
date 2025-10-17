class Solution:
  def reinitializePermutation(self, n: int) -> int:
    perm = [i for i in range(n)]
    ans = 0
    p = [v for v in perm]
    while True:
      ans += 1
      arr = [p[i//2] if i % 2 == 0 else p[n // 2 + (i-1)//2] for i in range(n)]
      if arr == perm:
        return ans
      else:
        p = arr
    return ans
        