class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = ''
        ord_0 = ord('0')
        ord_9 = ord('9')
        ans = set()
        for x in word:
            if ord_0 <= ord(x) <= ord_9:
                s += x
            else:
                if len(s) > 0:
                    ans.add(int(s))
                    s = ''
        if len(s) > 0:
            ans.add(int(s))
        return len(ans)
