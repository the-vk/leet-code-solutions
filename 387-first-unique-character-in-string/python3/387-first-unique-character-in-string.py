class Solution:
  def firstUniqChar(self, s: str) -> int:
    seen = {}
    for x in s:
      if x not in seen:
        seen[x] = 0
      seen[x] += 1
    for i, x in enumerate(s):
      if seen[x] == 1:
        return i
    return -1  