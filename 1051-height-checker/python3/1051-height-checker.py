class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        n = len(heights)
        expected = sorted(heights)
        ans = 0
        for i in range(n):
          if heights[i] != expected[i]:
            ans += 1
        return ans
