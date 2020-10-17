class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (self.n * 2)
        for i in range(self.n):
            self.tree[i+self.n] = nums[i]
        for i in range(self.n-1, -1, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2+1]

    def update(self, i: int, val: int) -> None:
        pos = i + self.n
        self.tree[pos] = val
        while pos > 0:
            left = right = pos
            if pos%2 == 0:
                right += 1
            else:
                left -= 1
            self.tree[int(pos/2)] = self.tree[left] + self.tree[right]
            pos = int(pos/2)

    def sumRange(self, i: int, j: int) -> int:
        left = i + self.n
        right = j + self.n
        sum = 0
        while left <= right:
            if left%2 == 1:
                sum += self.tree[left]
                left += 1
            if right%2 == 0:
                sum += self.tree[right]
                right -= 1
            left = int(left / 2)
            right = int(right/2)
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

