class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
      tails = [0] * len(nums)
      ans = 0
      for v in nums:
        i, j = 0, ans
        while i != j:
          m = (i + j) // 2
          if tails[m] < v:
            i = m + 1
          else:
            j = m
        tails[i] = v
        ans = max(ans, i + 1)
      return ans
