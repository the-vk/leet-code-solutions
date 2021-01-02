import time
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        prefix = 0
        while (prefix < min(len(strs[0]), len(strs[1])) and strs[0][prefix] == strs[1][prefix]):
            prefix += 1
        
        for i in range(2, len(strs)):
            prefix = min(prefix, min(len(strs[0]), len(strs[i])))
            while (prefix > 0 and strs[i][prefix-1] != strs[0][prefix-1]):
                prefix -= 1
            if prefix == 0:
                return ""
            
        return strs[0][0:prefix]        

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.longestCommonPrefix(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test("fl", ["flower","flow","flight"])
