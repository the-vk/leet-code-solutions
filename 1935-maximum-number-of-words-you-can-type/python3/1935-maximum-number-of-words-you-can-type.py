class Solution:
  def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
    letters = set()
    for x in brokenLetters:
      letters.add(x)
    ans = 0
    for w in text.split(' '):
      for l in w:
        if l in letters:
          ans -= 1
          break
      ans += 1
    return ans