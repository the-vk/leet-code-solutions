class Solution:
  def findArray(self, pref: List[int]) -> List[int]:
    res = [pref[0]] * len(pref)
    rolling = pref[0]
    for i in range(1, len(pref)):
      res[i] = pref[i] ^ rolling
      rolling ^= res[i]
    return res    
