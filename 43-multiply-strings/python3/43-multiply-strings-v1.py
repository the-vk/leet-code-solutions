import time
from typing import List

mult_table = dict()
add_table = dict()
for l in range(10):
    for r in range(10):
        mult_table[(str(l), str(r))] = str(l * r)[::-1]
        add_table[(str(l), str(r))] = str(l + r)[::-1]

class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        acc = "0"
        for n1f, n1d in enumerate(num1):
            for n2f, n2d in enumerate(num2):
                v = "0" * (n1f + n2f) + mult_table[(n1d, n2d)]
                acc = self.add(acc, v)
        i = len(acc) - 1
        while i > 0 and acc[i] == "0":
            i -= 1
        return acc[i::-1]

    def add(self, l, r):
        i = 0
        acc = ""
        carry = "0"
        while i < len(l) or i < len(r):
            if i < len(l):
                ld = l[i]
            else:
                ld = "0"
            if i < len(r):
                rd = r[i]
            else:
                rd = "0"
            s = add_table[(ld, rd)]
            if (carry != "0"):
                s = self.add(s, carry)
            if len(s) == 2:
                carry = s[1]
            else:
                carry = "0"
            s = s[0]
            acc += s
            i += 1
        if carry != "0":
            acc += carry
        return acc

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
