class Solution:
  def rearrangeArray(self, nums: List[int]) -> List[int]:
    positive = []
    negative = []
    n = len(nums)
    for v in nums:
      if v > 0:
        positive.append(v)
      else:
        negative.append(v)
    ans = [0] * n
    for i in range(n // 2):
      ans[i*2] = positive[i]
      ans[i*2+1] = negative[i]
    return ans

        