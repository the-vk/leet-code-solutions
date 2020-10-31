import time
from typing import List

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.storage = []

    def push(self, x: int) -> None:
        self.storage.append(x)

    def pop(self) -> int:
        return self.storage.pop()

    def top(self) -> int:
        return self.storage[-1]

    def peekMax(self) -> int:
        return max(self.storage)

    def popMax(self) -> int:
        max_item = self.peekMax()
        for i in range(len(self.storage) - 1, -1, -1):
            if self.storage[i] == max_item:
                self.storage.pop(i)
                break
        return max_item


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
        

def test(expected, *input):
    start = time.time_ns()
    try:
        solution = Solution()
        actual = solution.firstMissingPositive(*input)
        if actual != expected:
            print(f"actual value '{actual}' is not equal to expected value '{expected}'")
    finally:
        elapsed = (time.time_ns() - start) / (10 ** 9)
        print(f"elapsed: {elapsed} secs")
