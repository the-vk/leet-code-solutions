class Solution:
    def addBinary(self, a: str, b: str) -> str:
      l, r = [ self.stob(x) for x in [a, b]]
      return self.btos(l + r)

    def stob(self, s):
      r = 0
      for c in s:
        r = r << 1
        if c == '1':
          r = r | 1
      return r
    
    def btos(self, b):
      if b == 0:
        return "0"
      n = int(math.log(b, 2)) + 1
      r = [''] * n
      i = 0
      while i < n:
        r[i] = str((b & (1 << (n - i - 1))) >> (n - i - 1))
        i += 1
      return ''.join(r)