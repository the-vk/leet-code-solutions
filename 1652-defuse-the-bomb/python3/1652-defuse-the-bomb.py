class Solution:
  def decrypt(self, code: List[int], k: int) -> List[int]:
    n = len(code)
    plain = [0] * n
    if k == 0:
      return plain
 
    for i in range(len(code)):
      if k > 0:
        kk = k
        ii = (i+1) % n
        while kk > 0:
          plain[i] += code[ii]
          ii = (ii + 1) % n
          kk -= 1
      else:
        kk = -k
        ii = (i-1) % n
        while kk > 0:
          plain[i] += code[ii]
          ii = (ii - 1) % n
          kk -= 1

    return plain
