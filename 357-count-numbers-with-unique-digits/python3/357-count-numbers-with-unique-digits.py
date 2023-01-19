class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        result = 10
        uniq = 9
        available = 9
        while n > 1 and available > 0:
            uniq *= available
            result += uniq
            n -= 1
            available -= 1
        return result