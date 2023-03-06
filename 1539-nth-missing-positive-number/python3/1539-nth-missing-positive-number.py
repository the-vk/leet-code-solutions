class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
      s = set(arr)
      i = 0
      while k > 0:
        i += 1
        if i not in s:
          k -= 1
      return i