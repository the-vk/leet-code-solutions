import time
from typing import List
from heapq import heappush, heappop

class Ugly:
    def __init__(self):
        self.nums = []
        seen = set()
        heap = []
        heappush(heap, 1)
        for _ in range(1960):
            v = heappop(heap)
            self.nums.append(v)
            for i in [2,3,5]:
                next_ugly = v * i
                if next_ugly not in seen:
                    seen.add(next_ugly)
                    heappush(heap, next_ugly)

class Solution:
    u = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        return self.u.nums[n-1]
        

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

test(12, 10)
