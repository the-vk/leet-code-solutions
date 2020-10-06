import time
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        last_pos = dict()
        for i in range(len(s)):
            c = s[i]
            if c in last_pos:
                start = max(start, last_pos[c] + 1)
            last_pos[c] = i
            max_len = max(max_len, i - start + 1)
        return max_len


def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.lengthOfLongestSubstring(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
            raise ValueError("solution is invalid!")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test(3, "abcabcbb")
test(1, "bbbbb")
test(3, "pwwkew")
test(0, "")
test(2, "abba")

print("solution is correct!")
