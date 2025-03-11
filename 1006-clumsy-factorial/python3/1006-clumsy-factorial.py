class Solution:
    def clumsy(self, n: int) -> int:
        exp = str(n)
        op = ['*', '//', '+', '-']
        opi = 0
        for v in range(n-1, 0, -1):
          exp += op[opi % len(op)] + str(v)
          opi += 1
        return int(eval(exp))
