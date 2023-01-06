import time
from typing import List

class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        all_abbrs = dict()
        
        
def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.nthUglyNumber(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test(["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"], ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
