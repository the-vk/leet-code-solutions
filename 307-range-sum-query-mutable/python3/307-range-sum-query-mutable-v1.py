class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        sum = 0
        for x in range(i, j+1):
            sum += self.nums[x]
        return sum

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.robotSim(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")

