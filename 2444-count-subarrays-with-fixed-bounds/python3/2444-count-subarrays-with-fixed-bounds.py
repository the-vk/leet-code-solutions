class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      matches = []
      to_drop = []
      for r in range(len(haystack)):
        if haystack[r] == needle[0]:
          matches.append(r)
        for i in range(len(matches)):
          x = matches[i]
          if haystack[r] == needle[r-x] and (r-x) == (len(needle) - 1):
            return x
          if haystack[r] != needle[r-x]:
            to_drop.append(i)
        while to_drop:
          i = to_drop.pop()
          matches.pop(i)
      return -1