import time
from typing import List

class Solution:
    def simplifyPath(self, path: str) -> str:
        segments = path.split("/")
        out_segments = []
        for s in segments:
            if s == "" or s == ".":
                continue
            elif s == "..":
                if out_segments:
                    out_segments.pop()
            else:
                out_segments.append(s)
        return "/" + "/".join(out_segments)

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.simplifyPath(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test("/home", "/home/")
test("/", "/../")
test("/home/foo", "/home//foo/")
test("/c", "/a/./b/../../c/")
test("/c", "/a/../../b/../c//.//")
test("/a/b/c", "/a//b////c/d//././/..")