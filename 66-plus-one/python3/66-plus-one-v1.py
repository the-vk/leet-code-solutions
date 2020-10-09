import time
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        N = len(digits) - 1
        for i, v in enumerate(digits[::-1]):
            (digits[N-i], carry) = ((v+carry)%10, int((v+carry)/10))
        if carry != 0:
            digits.insert(0, 1)
        return digits

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.plusOne(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
            # raise ValueError("solution is invaid!")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test([1,2,4], [1,2,3])
test([4,3,2,2], [4,3,2,1])
test([1], [0])
test([1,0,0], [9,9])

print("solution is correct!")
