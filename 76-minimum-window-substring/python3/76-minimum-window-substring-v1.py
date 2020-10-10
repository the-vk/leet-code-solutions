import time
from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = dict()
        seen = dict()
        expecting = set(t)
        for v in t:
            seen[v] = 0
            if v in counter:
                counter[v] += 1
            else:
                counter[v] = 1
        
        left = right = 0
        window = (left, len(s))
        while right < len(s):
            while len(expecting) > 0 and right < len(s):
                r = s[right]
                if r in counter:
                    seen[r] += 1
                    if r in expecting and seen[r] >= counter[r]:
                        expecting.remove(r)
                right += 1
            while len(expecting) == 0:
                (wl, wr) = window
                if (right - left) < (wr - wl):
                    window = (left, right)
                l = s[left]
                if l in seen:
                    seen[l] -= 1
                    if l not in expecting and seen[l] < counter[l]:
                        expecting.add(l)
                left += 1
        if window == (left, len(s)):
            return ""
        else:
            (wl, wr) = window
            return s[wl:wr]        

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.minWindow(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test("a", "ab", "a")
test("BANC", "ADOBECODEBANC", "ABC")
test("a", "a", "a")
test("aa", "aa", "aa")
