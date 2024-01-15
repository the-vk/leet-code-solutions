class Solution:
  def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    players = set()
    losses = defaultdict(int)
    for (w, l) in matches:
      players.add(w)
      players.add(l)
      losses[l] += 1
    ans = [[], []]
    for p in players:
      if p not in losses:
        ans[0].append(p)
      else:
        if losses[p] == 1:
          ans[1].append(p)
    ans[0] = sorted(ans[0])
    ans[1] = sorted(ans[1])
    return ans
