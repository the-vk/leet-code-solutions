class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        l = 0
        while l < (n-1) and nums[l] <= nums[l+1]:
            l += 1
        r = n - 1
        while r > 0 and nums[r-1] <= nums[r]:
            r -= 1
        print (l, r)
        return (l == (n-1) and r == 0) or (l == (r-1) and nums[0] >= nums[-1])
