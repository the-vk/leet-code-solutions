class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
      banned = [x.lower() for x in banned]
      for x in "!?',;.'":
        paragraph = paragraph.replace(x, ' ')
      words = paragraph.split()
      c = {}
      for w in words:
        w = w.lower()
        if w not in c:
          c[w] = 0
        c[w] += 1
      m, mw = 0, None
      for k, v in c.items():
        if k in banned:
          continue
        if v > m:
          m = v
          mw = k
      return mw
