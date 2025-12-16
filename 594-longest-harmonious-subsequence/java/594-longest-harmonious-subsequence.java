class Solution {
  public int findLHS(int[] nums) {
    int l = 0, r = 0;
    var list = Arrays.stream(nums).sorted().toArray();
    var result = 0;
    while (l < list.length && r < list.length) {
      var d = list[r] - list[l];
      if (d == 0) {
        ++r;
      } else if (d == 1) {
        result = Math.max(result, r - l + 1);
        ++r;
      } else {
        ++l;
      }
    }

    return result;
  }
