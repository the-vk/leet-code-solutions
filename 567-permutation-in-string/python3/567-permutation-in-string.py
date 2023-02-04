class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = {}
        for x in s1:
            perm[x] = perm.get(x, 0) + 1
        l = r = 0
        c = perm.copy()
        while r < len(s2):
            if s2[r] in c:
                c[s2[r]] -= 1
                if r - l + 1 == len(s1):
                    match = True
                    for x in c.values():
                        match = match and (x == 0)
                    if match:
                        return True
                    else:
                        c[s2[l]] += 1
                        l += 1
                r += 1
            else:
                l += 1
                r = l
                c = perm.copy()
        return False