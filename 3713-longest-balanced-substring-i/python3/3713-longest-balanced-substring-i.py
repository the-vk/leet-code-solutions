class Solution(object):
  def longestBalanced(self, s):
    def isBalanced(ctr):
      val = None
      for f, v in ctr.items():
        if val == None:
          val = v
        else:
          if val != v:
            return False
      return True

    l = r = 0
    answer = 0

    while l < len(s):
      ctr = {}
      r = l
      while r < len(s):
        c = s[r]
        ctr[c] = 1 + ctr.get(c, 0)
        if isBalanced(ctr):
         answer = max(answer, r - l + 1)
        r += 1
      l += 1    

    return answer

