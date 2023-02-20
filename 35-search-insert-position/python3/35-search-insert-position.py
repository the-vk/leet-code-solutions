class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if target <= nums[l]:
          return l
        if target == nums[r]:
          return r
        if target > nums[r]:
          return len(nums)
        while r - 1 > l:
          m = (r - l) // 2 + l
          if target == nums[m]:
            return m
          if target < nums[m]:
            r = m
          else:
            l = m
        return r