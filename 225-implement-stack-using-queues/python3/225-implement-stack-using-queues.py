class MyStack:

    def __init__(self):
      self.q = deque()
      self.len = 0
        

    def push(self, x: int) -> None:
      self.len += 1
      self.q.appendleft((x, self.len))

    def pop(self) -> int:
      while self.q:
        x, p = self.q.pop()
        if p == self.len:
          self.len -= 1
          return x
        self.q.appendleft((x, p))

    def top(self) -> int:
      while self.q:
        x, p = self.q.pop()
        self.q.appendleft((x, p))
        if p == self.len:
          return x

    def empty(self) -> bool:
      return self.len == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()