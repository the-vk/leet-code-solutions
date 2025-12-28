class Solution {
  public int totalHammingDistance(int[] nums) {
    var ans = 0;
    var n = nums.length;
    for (var j = 0; j < 32; ++j) {
      var bitCount = 0;
      for (var i = 0; i < nums.length; ++i) {
        bitCount += (nums[i] >> j) & 1;
      }
      
      ans += bitCount * (n - bitCount);
    }
    return ans;
  }
}
