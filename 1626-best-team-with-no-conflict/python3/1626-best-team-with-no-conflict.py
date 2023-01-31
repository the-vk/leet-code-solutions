from operator import itemgetter, attrgetter

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = [(scores[i], ages[i]) for i in range(len(scores))]
        players = sorted(players, key=itemgetter(0))
        players = sorted(players, key=itemgetter(1))
        dp = [0] * len(scores)
        ans = 0
        for i in range(len(scores)):
            dp[i] = players[i][0]
            for j in range(i):
                if players[j][0] <= players[i][0]:
                    dp[i] = max(dp[i], dp[j] + players[i][0])
            ans = max(ans, dp[i])
        return ans