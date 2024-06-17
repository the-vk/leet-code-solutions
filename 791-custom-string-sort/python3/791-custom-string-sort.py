class Solution:
  def customSortString(self, order: str, s: str) -> str:
    lookup = {}
    for i, x in enumerate(order):
      lookup[x] = i
    return ''.join(sorted(s, key=lambda x: lookup.get(x, -1)))