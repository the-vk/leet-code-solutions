class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        for i, v in enumerate(nums):
            if v % 2 == 1:
                ans[i] = int(v - ((v+1) & (-v -1)) / 2)
        return ans
