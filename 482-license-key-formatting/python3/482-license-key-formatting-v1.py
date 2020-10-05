import time
from typing import List

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()
        out = []
        offset = len(S) % K
        if offset > 0:
            out.append(S[0:offset])
        for i in range(offset, len(S), K):
            out.append(S[i:i+K])
        return '-'.join(out)
        

def test(S, K, expected):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.licenseKeyFormatting(S, K)
        if actual != expected:
            raise ValueError(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test("5F3Z-2e-9-w", 4, "5F3Z-2E9W")
test("2-5g-3-J", 2, "2-5G-3J")

print("solution is correct!")
