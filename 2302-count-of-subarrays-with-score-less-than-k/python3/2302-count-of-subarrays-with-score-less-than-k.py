class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = r = result = current_sum = 0
        for r in range(len(nums)):
            current_sum += nums[r]

            while l <= r and current_sum * (r - l + 1) >= k:
              current_sum -= nums[l]
              l += 1
            result += (r - l + 1) 
        
        return result