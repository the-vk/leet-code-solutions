class Solution:
  def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
    def isStrictlyIncreasing(nums: List[int]) -> bool:
      ans = True
      for i in range(1, len(nums)):
        ans = ans and nums[i-1] < nums[i]
      return ans

    for i in range(len(nums) - k*2 + 1):
      if isStrictlyIncreasing(nums[i:i+k]) and isStrictlyIncreasing(nums[i+k:i+2*k]):
        return True
    return False