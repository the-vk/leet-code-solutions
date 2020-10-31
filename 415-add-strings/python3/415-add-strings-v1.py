import time
from typing import List

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        carry = 0
        li, ri = len(num1)-1, len(num2)-1
        while li >= 0 or ri >= 0:
            l = int(num1[li]) if li >= 0 else 0
            r = int(num2[ri]) if ri >= 0 else 0
            acc = l + r + carry
            v, carry = acc % 10, int(acc / 10)
            res += str(v)
            li -= 1
            ri -= 1
        if carry != 0:
            res += str(carry)
        return res[::-1]

        

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.addStrings(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test("2", "1", "1")
test("10", "1", "9")
test("7777", "2345", "5432")
test("10000", "9999", "1")
test("10000", "1", "9999")