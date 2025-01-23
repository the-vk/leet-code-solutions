class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        min_v = max_v = nums[0]
        min_i = max_i = 0
        for i, v in enumerate(nums):
            if v < min_v:
                min_v = v
                min_i = i
            if v > max_v:
                max_v = v
                max_i = i
        ans = min_i + n - max_i - 1
        if min_i > max_i:
            ans -= 1
        return ans