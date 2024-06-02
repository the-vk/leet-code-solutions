class Solution:
    def reverseString(self, s: List[str]) -> None:
        i, n = 0, len(s)
        while i < n/2:
          s[i], s[-i-1] = s[-i-1], s[i]
          i += 1
        