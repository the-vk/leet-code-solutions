class Solution:
  def isMonotonic(self, nums: List[int]) -> bool:
    mi = md = True
    for i in range(len(nums)-1):
      l, r = nums[i:i+2]
      mi = mi and l <= r
      md = md and l >= r
    return mi or md