from functools import reduce

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:        
        return reduce(lambda l, r: l | r, nums)