class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums): return "0"
        return "".join(sorted(map(str, nums), key=lambda x: x*(10), reverse=True))