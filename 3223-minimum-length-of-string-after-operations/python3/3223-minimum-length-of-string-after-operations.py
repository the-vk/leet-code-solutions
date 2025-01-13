class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        for _, c in c.items():
            while c >= 3:
                c -= 2
            ans += c
        return ans
