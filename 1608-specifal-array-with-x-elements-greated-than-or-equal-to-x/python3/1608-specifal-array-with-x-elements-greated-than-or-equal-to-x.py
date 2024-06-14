class Solution:
  def specialArray(self, nums: List[int]) -> int:
    cnt = [0] * 1001
    for x in nums:
      for i in range(x+1):
        cnt[i] += 1
    for i, x in enumerate(cnt):
      if i == x:
        return i
    return -1
