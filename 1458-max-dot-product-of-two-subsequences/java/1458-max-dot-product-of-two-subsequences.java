class Solution {
  public int maxDotProduct(int[] nums1, int[] nums2) {
    if (nums1.length < nums2.length) {
      return maxDotProduct(nums2, nums1);
    }
    
    int[][] dp = new int[2][501];
    for (var i = 0; i < dp.length; ++i) {
      for (var j = 0; j < dp[i].length; ++j) {
        dp[i][j] = Integer.MIN_VALUE;
      }
    }

    var res = Integer.MIN_VALUE;
    for (var i = nums1.length - 1; i >= 0; --i) {
      for (var j = nums2.length - 1; j >= 0; --j) {
        var x = nums1[i] * nums2[j];
        var tmp = dp[i & 1][j];
        tmp = Integer.max(tmp, x);
        tmp = Integer.max(tmp, x + (i + 1 < nums1.length && j + 1 < nums2.length ? dp[(i+1)&1][j+1] : 0));
        tmp = Integer.max(tmp, dp[i&1][j+1]);
        dp[i&1][j] = Integer.max(tmp, dp[(i+1)&1][j]);
        res = Integer.max(res, dp[i&1][j]);
      }
    }

    return res;
  }
}
