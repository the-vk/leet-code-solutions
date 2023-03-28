class CustomStack:

    def __init__(self, maxSize: int):
        self.data = [0] * maxSize
        self.pointer = 0

    def push(self, x: int) -> None:
        if self.pointer == len(self.data):
          return None
        self.data[self.pointer] = x
        self.pointer += 1

    def pop(self) -> int:
      if self.pointer == 0:
        return -1
      self.pointer -= 1
      return self.data[self.pointer]
        

    def increment(self, k: int, val: int) -> None:
        for x in range(0, min(k, self.pointer)):
          self.data[x] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)