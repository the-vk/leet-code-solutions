from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return not k>len(s) and sum(v&1 for v in Counter(s).values())<=k
