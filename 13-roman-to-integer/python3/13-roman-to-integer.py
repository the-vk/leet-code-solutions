import time
from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        def lookahead_c(c, pos, ans):
            if (pos == len(s) - 1):
                return (ans + 100, pos + 1)
            n = s[pos + 1]
            if (n == "D"):
                return (ans + 400, pos + 2)
            elif (n == "M"):
                return (ans + 900, pos + 2)
            else:
                return (ans + 100, pos + 1)
        
        def lookahead_x(c, pos, ans):
            if (pos == len(s) - 1):
                return (ans + 10, pos + 1)
            n = s[pos + 1]
            if (n == "L"):
                return (ans + 40, pos + 2)
            elif (n == "C"):
                return (ans + 90, pos + 2)
            else:
                return (ans + 10, pos + 1)
        
        def lookahead_i(c, pos, ans):
            if (pos == len(s) - 1):
                return (ans + 1, pos + 1)
            n = s[pos + 1]
            if (n == "V"):
                return (ans + 4, pos + 2)
            elif (n == "X"):
                return (ans + 9, pos + 2)
            else:
                return (ans + 1, pos + 1)
        
        ans = 0
        pos = 0
        while pos < len(s):
            c = s[pos]
            if (c == "M"):
                ans += 1000
                pos += 1
            elif (c == "D"):
                ans += 500
                pos += 1
            elif (c == "V"):
                ans += 5
                pos += 1
            elif (c == "L"):
                ans += 50
                pos += 1
            elif (c == "C"):
                (ans, pos) = lookahead_c(c, pos, ans)
            elif (c == "X"):
                (ans, pos) = lookahead_x(c, pos, ans)
            elif (c == "I"):
                (ans, pos) = lookahead_i(c, pos, ans)
            else:
                raise "invalid roman number "
        return ans
                

        

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.romanToInt(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test(1994, "MCMXCIV")
