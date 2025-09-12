VOWELS = {'a', 'e', 'i', 'o', 'u'}

class Solution:
  def doesAliceWin(self, s: str) -> bool:
    return sum([1 if v in VOWELS else 0 for v in s]) != 0
