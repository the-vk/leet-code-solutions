import time
from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def are_couple(l, r):
            if l % 2 == 0:
                return r == l + 1
            else:
                return r == l - 1

        N = len(row)
        people = dict()
        seats = list()
        swaps = 0
        for i in range(0, N, 2):
            l, r = row[i], row[i+1]
            people[l], people[r] = i, i+1
            if not are_couple(l, r):
                seats.append(i)
        for i in seats:
            l, r = row[i], row[i+1]
            if are_couple(l, r):
                continue
            if l % 2 == 0:
                sm = l + 1
            else:
                sm = l - 1
            row[people[sm]], row[i+1] = r, sm
            people[sm], people[r] = i+1, people[sm]
            swaps += 1

        return swaps

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.minSwapsCouples(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test(1, [0, 2, 1, 3])
test(0, [3, 2, 0, 1])
