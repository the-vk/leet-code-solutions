class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
      s = str(num)
      n = len(s)
      ans = 0
      for i in range(n-(k-1)):
        ss = s[i:i+k]
        d = int(ss)
        if d == 0:
          continue
        if num % d == 0:
          ans += 1
      return ans
        