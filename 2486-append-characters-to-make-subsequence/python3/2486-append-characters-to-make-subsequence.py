class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
      s_pos = 0
      t_pos = 0
      while s_pos < len(s) and t_pos < len(t):
        if s[s_pos] == t[t_pos]:
          t_pos += 1
        s_pos += 1
      return len(t) - t_pos
        