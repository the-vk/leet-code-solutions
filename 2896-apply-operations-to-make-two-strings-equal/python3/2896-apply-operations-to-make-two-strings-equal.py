class Solution:
  def minOperations(self, s1: str, s2: str, x: int) -> int:
    done, one, last, two = 0, inf, inf, inf
    for a,b in zip(s1, s2):
      if a == b:
        last, two = last + 1, two + 1
      else:
        done, one, last, two = min(one + x, last + 1), min(done, two + 1), min(done, two + x), one
    return done if done < inf else -1