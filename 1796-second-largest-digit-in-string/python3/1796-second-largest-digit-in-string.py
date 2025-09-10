class Solution:
    def secondHighest(self, s: str) -> int:
        store = set()
        for v in s:
          if v.isdigit():
            store.add((int(v)))
        arr = sorted(list(store))
        if len(arr) < 2:
          return -1
        return arr[-2]