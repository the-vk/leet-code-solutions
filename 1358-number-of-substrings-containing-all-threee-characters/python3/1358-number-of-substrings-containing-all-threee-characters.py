class Solution:
  def numberOfSubstrings(self, s: str) -> int:
    n = len(s)
    if n < 3:
      return 0

    pos = { 'a': deque(), 'b': deque(), 'c': deque() }
    for i, v in enumerate(s):
      pos[v].append(i)
    ans = 0
    

    for i, v in enumerate(s):
      if len(pos['a']) == 0 or len(pos['b']) == 0 or len(pos['c']) == 0:
        break
      ans += n - max(pos['a'][0], pos['b'][0], pos['c'][0])
      pos[v].popleft()
    
    return ans
