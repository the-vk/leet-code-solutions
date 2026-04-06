class Solution:
  def longestCommonPrefix(self, words: List[str]) -> List[int]:
    n = len(words)

    if n == 1:
      return [0]

    def pref(l, r):
      n = min(len(l), len(r))
      i = 0
      while i < n:
        if l[i] != r[i]:
          return i
        i += 1

      return i

    suffix = [0] * n
    prefix = [0] * n

    for i in range(n-2, -1, -1):
      suffix[i] = max(suffix[i+1], pref(words[i], words[i+1]))
    for i in range(1, n):
      prefix[i] = max(prefix[i-1], pref(words[i], words[i-1]))
    
    ans = [0] * n
    for i in range(n):
      if i == 0:
        ans[i] = suffix[i+1]
        continue
      
      if i == n-1:
        ans[i] = prefix[i-1]
        continue
      
      ans[i] = max(prefix[i-1], suffix[i+1], pref(words[i-1], words[i+1]))

    return ans
