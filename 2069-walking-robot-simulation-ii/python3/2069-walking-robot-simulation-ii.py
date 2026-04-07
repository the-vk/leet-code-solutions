class Robot:
  def __init__(self, width: int, height: int):
    self.width = width
    self.height = height
    self.loop = self.width * 2 + self.height * 2 - 4
    self.dirs = [
      [0, 1],
      [-1, 0],
      [0, -1],
      [1, 0]
    ]
    self.dirs_text = ['North', 'West', 'South', 'East']
    self.x = 0
    self.y = 0
    self.d = 3

  def step(self, num: int) -> None:
    if num >= self.loop:
      num %= self.loop
      if self.x == 0 and self.y == 0:
        self.d = 2
      if self.x == self.width-1 and self.y == 0:
        self.d = 3
      if self.x == self.width-1 and self.y == self.height - 1:
        self.d = 0
      if self.x == 0 and self.y == self.height - 1:
        self.d = 1
    while num > 0:
      d = self.dirs[self.d]
      self.x = self.x + d[0] * num
      self.y = self.y + d[1] * num

      if self.x < 0:
        num = -1*self.x
        self.x = 0
        self.d = (self.d + 1) % 4
        continue

      if self.x >= self.width:
        num = self.x - self.width + 1
        self.x = self.width - 1
        self.d = (self.d + 1) % 4
        continue

      if self.y < 0:
        num = -1*self.y
        self.y = 0
        self.d = (self.d + 1) % 4
        continue

      if self.y >= self.height:
        num = self.y - self.height + 1
        self.y = self.height - 1
        self.d = (self.d + 1) % 4
        continue

      break

  def getPos(self) -> List[int]:
    return [self.x, self.y]

  def getDir(self) -> str:
    return self.dirs_text[self.d]

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
