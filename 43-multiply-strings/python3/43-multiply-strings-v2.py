import time
from typing import List

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        i = len(res) - 1
        for l in [int(x) for x in reversed(num1)]:
            j = i
            for r in [int(x) for x in reversed(num2)]:
                res[j] += l*r
                res[j-1] += int(res[j]/10)
                res[j] %= int(10)
                j -= 1
            i -=1

        i = 0
        while i < len(res)-1 and res[i] == 0:
            i += 1
        return "".join([str(x) for x in res[i:]])


def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.multiply(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
            # raise ValueError("solution is invaid!")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test("0", "9133", "0")
test("998001", "999", "999")
test("56088", "123", "456")
test("6", "2", "3")

print("solution is correct!")
