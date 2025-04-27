class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2):
          l, m, r = nums[i:i+3]
          if (l + r) == (m / 2):
            ans += 1
        return ans