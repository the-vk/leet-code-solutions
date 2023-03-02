class Solution:
    def compress(self, chars: List[str]) -> int:
      r = 1
      w = 0
      s = chars[0]
      c = 1
      while r < len(chars):
        if chars[r] == s:
          c += 1
        else:
          s = chars[r]
          if c > 1:
            l = str(c)
            for x in l:
              w += 1
              chars[w] = x
          w += 1
          chars[w] = s
          c = 1
        r += 1
      if c > 1:
        l = str(c)
        for x in l:
          w += 1
          chars[w] = x
      return w+1