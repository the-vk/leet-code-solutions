import time
from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        roots = dict()
        for [s,e] in edges:
            if e in roots:
                ext = {e}.union(roots[e])
                if s in roots:
                    roots[s] = roots[s].union(ext)
                else:
                    roots[s] = ext
                del roots[e]
                continue
            if s not in roots:
                added = False
                for k,v in roots.items():
                    if s in v:
                        v.add(e)
                        added = True
                        break
                if not added:
                    roots[s] = {e}
            else:
                added = False
                for k,v in roots.items():
                    if s in v:
                        roots
                        v.add(e)
                        added = True
                        break
                if not added:
                    roots[s].add(e)
        return sorted(roots.keys())

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.findSmallestSetOfVertices(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test([3], 5, [[0,1],[3,2],[4,1],[2,1],[4,2],[3,4],[0,2],[4,0]])
test([0,3], 6, [[0,1],[0,2],[2,5],[3,4],[4,2]])
test([0,2,3], 5, [[0,1],[2,1],[3,1],[1,4],[2,4]])
