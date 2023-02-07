import time
from typing import List

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        n = len(tree)
        t1 = t2 = -1
        t1s = -1
        ans = 0;
        for i in range(n):
            t = tree[i]
            if t != t1 and t != t2:
                ans = max(ans, i - t1s)
                t1s = i
                while (t1s > 0 and tree[t1s - 1] == tree[i - 1]):
                    t1s -= 1
                t1 = tree[i - 1]
                t2 = t
        ans = max(ans, n - t1s)
        return ans

def test(tree, expected):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.totalFruit(tree)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
            raise ValueError("solution is invalid!")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test([1,2,1], 3)
test([0,1,2,2], 3)
test([1,2,3,2,2], 4)
test([3,3,3,1,2,1,1,2,3,3,4], 5)
test([1,1,6,5,6,6,1,1,1,1], 6)

print("solution is correct!")
