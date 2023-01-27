class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        roots = { w for w in words }
        res = []
        for w in words:
            n = len(w)
            dp = [0] * (n+1)
            dp[0] = 1
            for i in range(n):
                if dp[i] == 0:
                    continue
                for j in range(i+1, n+1):
                    if j-i != n and w[i:j] in roots:
                        dp[j] = 1
            if dp[n] == 1:
                res.append(w)
        return res
