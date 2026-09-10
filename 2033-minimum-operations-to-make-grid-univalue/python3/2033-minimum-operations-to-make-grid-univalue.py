class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        vals = sorted([x for xs in grid for x in xs])
        mi = len(vals) // 2
        m = vals[mi]
        ans = 0
        for v in vals:
            d = abs(m - v)
            if (d / x) == (d // x):
                ans += d // x
            else:
                return -1
        return ans
