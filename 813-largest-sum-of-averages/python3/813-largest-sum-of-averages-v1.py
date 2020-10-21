import time
from typing import List

class Solution(object):
    def largestSumOfAverages(self, A, K):
        P = [0]
        N = len(A)
        memo = dict()
        for x in A: P.append(x + P[-1])
        def average(i, j):
            return (P[j] - P[i]) / float(j - i)
        def rec(s, k):
            if (s,k) in memo:
                return memo[(s,k)]
            if k == 1:
                return average(s, N)
            num = 0
            for i in range(s+1, N-k+2):
                num = max(num, average(s, i) + rec(i, k-1))
            memo[(s,k)] = num
            return num
        return rec(0, K)
        

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.largestSumOfAverages(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test(20, [9,1,2,3,9], 3)
test(167436.0833333333, [4663,3020,7789,1627,9668,1356,4207,1133,8765,4649,205,6455,8864,3554,3916,5925,3995,4540,3487,5444,8259,8802,6777,7306,989,4958,2921,8155,4922,2469,6923,776,9777,1796,708,786,3158,7369,8715,2136,2510,3739,6411,7996,6211,8282,4805,236,1489,7698], 27)
