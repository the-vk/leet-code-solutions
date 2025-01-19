class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        c = [n] * n
        sA = set(A)
        sB = set(B)
        for x in range(n-2, -1, -1):
            sA.remove(A[x+1])
            sB.remove(B[x+1])
            c[x] = len(sA & sB)
        return c
        