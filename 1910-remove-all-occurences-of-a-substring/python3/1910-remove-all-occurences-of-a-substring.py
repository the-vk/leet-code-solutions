class Solution:
  def removeOccurrences(self, s: str, part: str) -> str:
    n = len(part)
    i = i = s.find(part)
    while i >= 0:
      if s == 0:
        s = s[n:]
      else:
        s = s[0:i] + s[i+n:]
      i = i = s.find(part)
    return s