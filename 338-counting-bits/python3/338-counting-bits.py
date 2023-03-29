class Solution:
    def countBits(self, n: int) -> List[int]:
      ans = [0] * (n+1)
      for i in range(len(ans)):
        x = 1
        while x <= i:
          if (x & i) > 0:
            ans[i] += 1
          x = x << 1
      return ans