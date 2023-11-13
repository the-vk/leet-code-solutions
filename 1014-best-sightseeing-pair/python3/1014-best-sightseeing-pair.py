class Solution:
  def maxScoreSightseeingPair(self, values: List[int]) -> int:
    max_val = values[0]
    min_val = 1001 
    res = 0
    for i in range(1, len(values)):
      min_val = values[i] - i
      res = max(res, max_val + min_val)
      max_val = max(max_val, values[i] + i)
    return res