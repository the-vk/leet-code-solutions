class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lookup = { k: i for i, k in enumerate(order) }
        print(lookup)
        for i in range(len(words) - 1):
            l, r = words[i], words[i+1]
            for x in range(max(len(l), len(r))):
                if x == len(l):
                    break
                if x == len(r):
                    return False
                li = lookup[l[x]]
                ri = lookup[r[x]]
                if li < ri:
                    break
                if li > ri:
                    print(x)
                    return False
        return True