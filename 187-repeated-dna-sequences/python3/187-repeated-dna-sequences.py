class Solution:
  def findRepeatedDnaSequences(self, s: str) -> List[str]:
    seen = set()
    ans_s = set()
    ans = []
    for i in range(len(s)-9):
      ss = s[i:i+10]
      h = hash(ss)
      if h in seen:
        if h not in ans_s:
          ans.append(ss)
          ans_s.add(h)
      else:
        seen.add(h)
    return ans