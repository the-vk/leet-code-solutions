class Solution {
  public int[] minBitwiseArray(List<Integer> nums) {
    int[] ans = new int[nums.size()];

    for (var i = 0; i < nums.size(); ++i) {
      for (var x = 0; x < nums.get(i); ++x) {
        if ((x | (x + 1)) == nums.get(i)) {
          ans[i] = x;
          break;
        } else {
          ans[i] = -1;
        }
      }
    }

    return ans;
  }
}
