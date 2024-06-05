class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
      cnt = [101] * 26
      for w in words:
        w_cnt = [0] * 26
        for l in w:
          w_cnt[ord(l) - ord('a')] += 1
        for i in range(26):
          cnt[i] = min(cnt[i], w_cnt[i])
      ans = []
      for i, v in enumerate(cnt):
        for x in range(v):
          ans.append(chr(i + ord('a')))
      return ans
