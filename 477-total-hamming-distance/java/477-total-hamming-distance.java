class Solution {
  public int totalHammingDistance(int[] nums) {
    var ans = 0;
    for (var i = 0; i < nums.length; ++i) {
      for (var j = i + 1; j < nums.length; ++j) {
        ans += Integer.bitCount(nums[i] ^ nums[j]);
      }
    }
    return ans;
  }
}

