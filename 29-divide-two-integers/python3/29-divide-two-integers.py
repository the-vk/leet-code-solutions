class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        isPositive = (dividend < 0) == (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)
        ans = 0
        while a >= b:
            q = 0
            while a > (b << (q+1)):
                q += 1
            ans += (1 << q)
            a = a - (b << q)
        if ans == (1 << 31) and isPositive:
            return 2 ** 31 - 1
        return ans if isPositive else -ans