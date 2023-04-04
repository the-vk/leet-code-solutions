class Solution:
    def partitionString(self, s: str) -> int:
      seen = set()
      ans = 1
      for x in range(len(s)):
        l = s[x]
        if l in seen:
          ans += 1
          seen = set()
        seen.add(l)
      return ans
