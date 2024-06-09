class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
      ans = [0] * len(nums)
      i = 0
      while i < len(nums) - 1:
        if abs(nums[i]) < abs(nums[i+1]):
          break
        i += 1
      l = i
      r = l + 1
      i = 0
      while l >= 0 and r <= len(nums) - 1:
        ans[i] = min(abs(nums[l]), abs(nums[r])) ** 2
        if abs(nums[l]) < abs(nums[r]):
          l -= 1
        else:
          r += 1
        i += 1
      while l > -1:
        ans[i] = nums[l] ** 2
        i += 1
        l -= 1
      while r < len(nums):
        ans[i] = nums[r] ** 2
        i += 1
        r += 1
      return ans

        