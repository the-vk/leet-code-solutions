class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        n = len(ideas)
        originals = set(ideas)
        parts = {}
        for x in ideas:
            h, t = x[0], x[1:]
            l = parts.get(h, set())
            l.add(t)
            parts[h] = l
        ans = 0
        keys = list(parts.keys())
        for i in range(len(keys) - 1):
            for j in range(i + 1, len(keys)):
                s = parts[keys[i]] | parts[keys[j]]
                ans += 2 * (len(s) - len(parts[keys[i]])) * (len(s) - len(parts[keys[j]]))

        return ans