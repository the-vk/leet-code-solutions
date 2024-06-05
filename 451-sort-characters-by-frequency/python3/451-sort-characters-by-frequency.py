class Solution:
  def frequencySort(self, s: str) -> str:
    tally = {}
    for l in s:
      if l not in tally:
        tally[l] = 0
      tally[l] += 1
    ans = ''
    for l, c in sorted(tally.items(), key=itemgetter(1), reverse=True):
      for x in range(c):
        ans += l
    return ans