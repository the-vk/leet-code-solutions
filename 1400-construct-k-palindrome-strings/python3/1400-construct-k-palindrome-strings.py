class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        ctr = {}
        for v in s:
            if v in ctr:
                ctr[v] += 1
            else:
                ctr[v] = 1
        odd_count = 0
        for _, v in ctr.items():
            if v % 2 == 1:
                odd_count += 1
        return odd_count == 0 or odd_count <= k