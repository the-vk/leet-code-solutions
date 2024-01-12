class Solution:
    def halvesAreAlike(self, s: str) -> bool:
      vowels = set('aeiou')
      s = s.lower()
      a, b = s[0:len(s)//2], s[len(s)//2:]
      a_c = b_c = 0
      for i in range(len(a)):
        if a[i] in vowels:
          a_c += 1
        if b[i] in vowels:
          b_c += 1
      return a_c == b_c
