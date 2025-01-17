class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        c = 0
        for v in derived:
            c ^= v
        return c == 0