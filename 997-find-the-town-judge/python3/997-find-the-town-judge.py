class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        t = {}
        for a, b in trust:
            s = t.get(a, set())
            s.add(b)
            t[a] = s
        if len(t) != n - 1:
            return -1
        head, *tail = t.values()
        s = set(head)
        for x in tail:
            s = s & set(x)
        if len(s) != 1:
            return -1
        return s.pop()
