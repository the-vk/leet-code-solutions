class Solution:
  def addDigits(self, num: int) -> int:
    while num > 9:
      n = 0
      while num > 0:
        n += num % 10
        num = int(num / 10)
      num = n
    return num