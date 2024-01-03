class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
      lines = []
      for r in bank:
        lines.append(0)
        for c in r:
          if c == '1':
            lines[-1] += 1
        if lines[-1] == 0:
          lines.pop()
      ans = 0
      for i in range(len(lines)-1):
        ans += lines[i] * lines[i+1]
      return ans
