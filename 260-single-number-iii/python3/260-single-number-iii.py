class Solution:
  def singleNumber(self, nums: List[int]) -> List[int]:
    n = 0
    for x in nums:
      n ^= x

    d = n & -n
    
    ans = [0, 0]
    for x in nums:
      if (d & x) == 0:
        ans[0] ^= x
      else:
        ans[1] ^= x
    
    return ans