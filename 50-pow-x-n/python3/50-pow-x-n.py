class Solution:
  def myPow(self, x: float, n: int) -> float:
    ans = 1
    k = abs(n)

    while k > 0:
      if k % 2 == 0:
        x *= x
        k /= 2
      else:
        ans = ans * x
        k -= 1
    
    return ans if n > 0 else 1.0 / ans
