class Solution {
  public int duplicateNumbersXOR(int[] nums) {
    var result = 0;
    var seen = new HashSet<Integer>();

    for (var i = 0; i < nums.length; ++i) {
      var n = nums[i];
      if (!seen.contains(n)) {
        seen.add(n);
      } else {
        result ^= n;
      }
    }

    return result;
  }
}