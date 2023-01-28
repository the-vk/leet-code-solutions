class SummaryRanges:

    def __init__(self):
        self.arr = [False] * 10000

    def addNum(self, value: int) -> None:
        self.arr[value] = True

    def getIntervals(self) -> List[List[int]]:
        res = []
        start = -1
        for end in range(len(self.arr)):
            if self.arr[end]:
                if start == -1:
                    start = end
            else:
                if start != -1:
                    res.append([start, end-1])
                    start = -1

        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()