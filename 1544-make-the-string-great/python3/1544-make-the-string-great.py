class Solution:
    def makeGood(self, s: str) -> str:
      def notGood(l, r):
        return l != r and l.lower() == r.lower()
      i = 0
      while i >= 0 and i < len(s) - 1:
        if notGood(s[i], s[i+1]):
          s = s[:i] + s[i+2:]
          i = max(i-1, 0)
          continue
        i += 1
      return s
        