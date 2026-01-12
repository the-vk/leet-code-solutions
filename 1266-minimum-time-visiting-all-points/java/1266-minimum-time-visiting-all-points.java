class Solution {
  public int minTimeToVisitAllPoints(int[][] points) {
    var ans = 0;
    for (var i = 0; i < points.length - 1; ++i) {
      var p = points[i];
      var n = points[i+1];

      var dx = n[0] - p[0];
      var dy = n[1] - p[1];

      ans += Integer.max(Math.abs(dx), Math.abs(dy));
    }

    return ans;
  }
}
