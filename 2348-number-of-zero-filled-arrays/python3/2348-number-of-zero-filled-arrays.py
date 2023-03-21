class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
      ans, c = 0, 1
      for i in range(len(nums)):
        if nums[i] == 0:
          ans += c
          c += 1
        else:
          c = 1
      return ans
