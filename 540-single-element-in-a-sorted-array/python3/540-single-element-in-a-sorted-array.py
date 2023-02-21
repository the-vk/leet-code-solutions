class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
      l = 0
      r = len(nums) - 1
      while l != r:
        m = (r - l) // 2 + l
        print("l", l, "r", r, "m", m)
        if m == 0 or m == len(nums) - 1:
          return nums[m]
        if nums[m-1] != nums[m] and nums[m] != nums[m+1]:
          return nums[m]
        if nums[m-1] == nums[m]:
          if m % 2 == 0:
            r = m
          else:
            l = m + 1
        else:
          if m % 2 == 0:
            l = m + 1
          else:
            r = m
      return nums[l]