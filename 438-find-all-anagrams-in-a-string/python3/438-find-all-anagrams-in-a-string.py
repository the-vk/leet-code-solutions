class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if (len(s) < len(p)):
            return []
        sHash = {}
        pHash = {}
        for x in p:
            pHash[x] = pHash.get(x, 0) + 1

        for i in range(len(p)):
            x = s[i]
            sHash[x] = sHash.get(x, 0) + 1

        res = []
        match = True
        for k, v in pHash.items():
            match = match and (k in sHash and sHash[k] == pHash[k])
        if match:
            res.append(0)

        for i in range(len(p), len(s)):
            pl, nl = s[i-len(p)], s[i]
            sHash[pl] -= 1
            if sHash[pl] == 0:
                del sHash[pl]
            sHash[nl] = sHash.get(nl, 0) + 1
            match = True
            for k, v in pHash.items():
                match = match and (k in sHash and sHash[k] == pHash[k])
            if match:
                res.append(i - len(p) + 1)
        return res