class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        v = set(nums)
        for f in range(1, 102):
            if (k*f) not in v:
                return k*f
        return -1