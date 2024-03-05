from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = defaultdict(int)
        for x in s:
          count[x] += 1
        c = None
        for k, v in count.items():
          if c == None:
            c = v
          if c != v:
            return False
        return True