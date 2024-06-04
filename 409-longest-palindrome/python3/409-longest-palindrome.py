class Solution:
    def longestPalindrome(self, s: str) -> int:
      l = defaultdict(int)
      for k in s:
        l[k] += 1
      ans = 0
      has_odd = False
      for v in l.values():
        ans += v - v % 2
        if v % 2 == 1 and not has_odd:
          ans += 1
          has_odd = True
      return ans