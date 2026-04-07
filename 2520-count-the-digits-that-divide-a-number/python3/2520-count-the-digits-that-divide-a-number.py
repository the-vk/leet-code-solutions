class Solution:
  def countDigits(self, num: int) -> int:
    return len([True for x in str(num) if num % int(x) == 0])
        
