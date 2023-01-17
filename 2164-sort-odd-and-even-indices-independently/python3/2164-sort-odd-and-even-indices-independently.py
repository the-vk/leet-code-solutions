class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = sorted([nums[x] for x in range(0, len(nums), 2)])
        odds = sorted([nums[x] for x in range(1, len(nums), 2)], reverse=True)
        for x in range(len(nums)):
            nums[x] = evens[x//2] if x % 2 == 0 else odds[x//2]
        return nums