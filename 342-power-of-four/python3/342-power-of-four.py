class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        v = math.log(n, 4)
        return v == int(v)