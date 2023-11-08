from collections import deque

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
      n = len(nums1)
      res = [0] * n
      nums1 = sorted(nums1)
      p = sorted([(x, i) for (i, x) in enumerate(nums2)], key=lambda v: v[0])
      fp, lp = 0, n-1
      for x in nums1:
        if p[fp][0] < x:
          res[p[fp][1]] = x
          fp += 1
        else:
          res[p[lp][1]] = x
          lp -= 1
      return res
