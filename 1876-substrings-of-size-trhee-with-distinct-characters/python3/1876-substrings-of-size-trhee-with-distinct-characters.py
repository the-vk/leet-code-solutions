class Solution:
  def countGoodSubstrings(self, s: str) -> int:
    ans = 0
    chars = defaultdict(int)
    l = r = 0
    while r < len(s):
      chars[s[r]] += 1
      if (r - l) == 3:
        chars[s[l]] -= 1
        if chars[s[l]] == 0:
          del chars[s[l]]
        l += 1
      if len(chars) == 3:
        ans += 1
      r += 1
    return ans