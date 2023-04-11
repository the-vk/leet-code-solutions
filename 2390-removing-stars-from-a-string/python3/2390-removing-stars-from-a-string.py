class Solution:
    def removeStars(self, s: str) -> str:
      st = []
      for x in s:
        if x == '*':
          st.pop()
        else:
          st.append(x)
      return ''.join(st)