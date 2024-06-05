class Solution:
  def findMaxK(self, nums: List[int]) -> int:
    def cmp(l, r):
      print(l, r)
      if l == r:
        return 0
      if l < r:
        return -1
      else:
        return 1
  
    nums = sorted(nums)
    l = 0
    r = len(nums) - 1
    while l < r and nums[l] != nums[r]:
      match cmp(abs(nums[l]), nums[r]):
        case -1:
          r -= 1
        case 0:
          return nums[r]
        case 1:
          l += 1
    return -1