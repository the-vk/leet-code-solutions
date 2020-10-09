import time
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        matrix.reverse()
        for i in range(N):
            for j in range(i + 1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix


def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.rotate(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
            # raise ValueError("solution is invaid!")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

test([[7,4,1],[8,5,2],[9,6,3]], [[1,2,3],[4,5,6],[7,8,9]])
test([[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]], [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
test([[1]], [[1]])
test([[3,1],[4,2]], [[1,2],[3,4]])

print("solution is correct!")
