class Solution:
  def maxLength(self, arr: List[str]) -> int:
    def iscompat(l, r):
      return len(set(l) | set(r)) == len(l) + len(r)
    compat = {}
    for i, l in enumerate(arr):
      if len(l) != len(set(l)):
        continue
      if l not in compat:
        compat[l] = set()
      for r in arr[i+1:]:
        if iscompat(l, r):
          compat[l].add(r)
    def walk(i, s):
      v = arr[i]
      if v not in compat:
        return 0
      ans = len(v)
      for x in s:
        if x not in compat or v not in compat[x]:
          return 0
      for xi in range(i+1, len(arr)):
        ans = max(ans, len(v) + walk(xi, s + [v]))
      return ans
    return max([walk(i, []) for i in range(len(arr))])
      