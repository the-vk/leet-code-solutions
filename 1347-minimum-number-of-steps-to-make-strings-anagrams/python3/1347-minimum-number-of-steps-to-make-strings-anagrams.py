class Solution:
    def minSteps(self, s: str, t: str) -> int:
      def count_letters(st):
        res = defaultdict(int)
        for v in st:
          res[v] += 1
        return res
      
      s_m = count_letters(s)
      t_m = count_letters(t)
      diff = 0
      for k in t_m:
        diff += abs(t_m[k] - s_m[k])
      for k in s_m:
        if k not in t_m:
          diff += s_m[k]
      return diff // 2
