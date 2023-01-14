class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = {}
        for w in s1.split() + s2.split():
            words[w] = words.get(w, 0) + 1
        return [k for (k, v) in words.items() if v == 1]