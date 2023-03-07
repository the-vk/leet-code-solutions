class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
      l = num
      r = []
      while k > 0:
        r.insert(0, k % 10)
        k = k // 10
      res = [0] * max(len(l), len(r))
      carry = 0
      for i in range(len(res) - 1, -1, -1):
        if i - (len(res) - len(l)) >= 0:
          li = l[i - (len(res) - len(l))]
        else:
          li = 0
        if i - (len(res) - len(r)) >= 0:
          ri = r[i - (len(res) - len(r))]
        else:
          ri = 0
        res[i] = li + ri + carry
        carry = res[i] // 10
        res[i] = res[i] % 10
      if carry != 0:
        res.insert(0, carry)
      return res