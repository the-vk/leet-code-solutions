import time
from typing import List

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        offset = {0: 0, 1: 1}
        off_off = [0] * (R+C)
        def get_offset(dist):
            if dist not in offset:
                res = get_offset(dist-1) + 4 * (dist-1)
                offset[dist] = res
            return offset[dist]
                    
        res = [None] * (get_offset(R+C))
        for x in range(R):
            for y in range(C):
                dist = abs(x - r0) + abs(y - c0)
                pos = offset[dist] + off_off[dist]
                off_off[dist] += 1
                res[pos] = [x, y]
        return [x for x in res if x != None]
        

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.allCellsDistOrder(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test([[0,0],[0,1]], 1, 2, 0, 0)
test([[0,1],[0,0],[1,1],[1,0]], 2, 2, 0, 1)
test([[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]], 2, 3, 1, 2)
test([[2, 5], [1, 5], [2, 4], [0, 5], [1, 4], [2, 3], [0, 4], [1, 3], [2, 2], [0, 3], [1, 2], [2, 1], [0, 2], [1, 1], [2, 0], [0, 1], [1, 0], [0, 0]], 3, 6, 2, 5)
