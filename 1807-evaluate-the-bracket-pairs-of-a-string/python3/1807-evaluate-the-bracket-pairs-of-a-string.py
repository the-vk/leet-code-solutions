class Solution:
  def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
    m = {k:v for k, v in knowledge}
    result = []
    i = 0
    while i < len(s):
      if s[i] == '(':
        j = s.index(')', i)
        key = s[i+1:j]
        result.append(m.get(key, '?'))
        i = j + 1
      else:
        result.append(s[i])
        i += 1

    return ''.join(result)
