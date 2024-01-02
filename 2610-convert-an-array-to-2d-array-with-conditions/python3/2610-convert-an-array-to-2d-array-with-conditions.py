from operator import itemgetter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
      lookup = {}
      for v in nums:
        if v not in lookup:
          lookup[v] = 1
        else:
          lookup[v] += 1
      pairs = sorted([[k, v] for (k,v) in lookup.items()], key=itemgetter(1), reverse=True)
      ans = []
      while pairs:
        ans.append([])
        for i in range(len(pairs)):
          ans[-1].append(pairs[i][0])
          pairs[i][1] -= 1
        while pairs and pairs[-1][1] == 0:
          pairs.pop()
      return ans
    